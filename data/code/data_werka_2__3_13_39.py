def convert_to_celsius(fahrenheit):
    return list(map(lambda f: (f - 32) * 5 / 9, fahrenheit))

if __name__ == '__main__':
    sample_temperatures = (32, 68, 100, 212)
    celsius_temperatures = convert_to_celsius(sample_temperatures)
    print(celsius_temperatures)