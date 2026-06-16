def celsius_to_fahrenheit(celsius_readings):
    fahrenheit_readings = []
    for c in celsius_readings:
        f = (c * 9/5) + 32
        fahrenheit_readings.append(f)
    return fahrenheit_readings
if __name__ == '__main__':
    sample_temps = [0, 10, 20, 25, 30]
    fahrenheit_temps = celsius_to_fahrenheit(sample_temps)
    print(fahrenheit_temps)