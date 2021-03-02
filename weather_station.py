class Subject:
    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered or removed.
    def registerObserver():
        pass

    def removeObserver():
        pass

    # This method is called to notify all observers
    # when the Subject's state (measurements) has changed.
    def notifyObservers():
        pass

# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and
# passing the measurements to the observers.
class Observer:
    def update(self, temp, humidity, pressure):
        pass

# WeatherData now implements the subject interface.
class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def registerObserver(self, observer):
        # When an observer registers, we just 
        # add it to the end of the list.
        self.observers.append(observer)

    def removeObserver(self, observer):
        # When an observer wants to un-register,
        # we just take it off the list.
        self.observers.remove(observer)

    def notifyObservers(self):
        # We notify the observers when we get updated measurements 
        # from the Weather Station.
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurementsChanged()

    # other WeatherData methods here.

class CurrentConditionsDisplay(Observer):
    def __init__(self, weatherData):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer 
                                           # so it gets data updates.
    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print("Current conditions:", self.temperature, 
              "F degrees and", self.humidity,"[%] humidity",
              "and pressure", self.pressure)

# TODO: implement StatisticsDisplay class and ForecastDisplay class.
class StatisticsDisplay:
    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.max = self.getMax()
        self.min = self.getMin()
        self.average = self.getAverage()

    def getMax(self):
        max = self.weather_data[0]
        for i in self.weather_data:
            if i > max:
                max = i
        return max

    def getMin(self):
        min = self.weather_data[0]
        for i in self.weather_data:
            if i < min:
                min = i
        return min

    def getAverage(self):
        return sum(self.weather_data) / len(self.weather_data)

    def display(self):
        print(f"Statistics: Max: {self.max} Min: {self.min} Average: {self.average}")

class ForecastDisplay:
    def __init__(self, temperature, humidity, pressure):
        self.temp = temperature + 0.11 * humidity + 0.2 * pressure
        self.humidity = humidity - 0.9 * humidity
        self.pressure = pressure + 0.1 * temperature - 0.21 * pressure

    def display(self):
        print(f"Temperature: {self.temp} Humidity: {self.humidity} Pressure: {self.pressure}")

class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)
        statistics_display = StatisticsDisplay(weather_data)
        statistics_display.display
        forcast_display = ForcastDisplay(temperature, humidity, pressure)
        forcast_display.display
        weather_data.setMeasurements(80, 65,30.4)
        weather_data.setMeasurements(82, 70,29.2)
        weather_data.setMeasurements(78, 90,29.2)

        # un-register the observer
        weather_data.removeObserver(current_display)
        weather_data.setMeasurements(120, 100,1000)


if __name__ == "__main__":
    w = WeatherStation()
    w.main()
