def convert_temp(celsius_readings):
    fahrenheit_readings = [c * 9/5 + 32 for c in celsius_readings]
    return fahrenheit_readings
if __name__ == '__main__':
    sample_temps = [0, 10, 20, 25, 30, 100]
    fahrenheit_temps = convert_temp(sample_temps)
    print(fahrenheit_temps)