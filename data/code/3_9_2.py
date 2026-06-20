def convert_temp(temperatures_c):
    return [c * 9 / 5 + 32 for c in temperatures_c]

if __name__ == '__main__':
    celsius_readings = [0, 100, 37, -40, 21.5]
    fahrenheit_readings = convert_temp(celsius_readings)
    print(fahrenheit_readings)