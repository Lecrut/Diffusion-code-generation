def celsius_to_fahrenheit(celsius_readings):
    fahrenheit_readings = {}
    for location, temp in celsius_readings.items():
        fahrenheit_readings[location] = (temp * 9 / 5) + 32
    return fahrenheit_readings

if __name__ == '__main__':
    readings = {
        "New York": 10,
        "London": 15,
        "Tokyo": 25
    }
    result = celsius_to_fahrenheit(readings)
    print(result)