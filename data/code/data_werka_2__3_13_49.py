def convert_to_celsius(fahrenheit):
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5 / 9
    return tuple(map(fahrenheit_to_celsius, fahrenheit))

if __name__ == '__main__':
    sample_temperatures = (0, 32, 68, 100)
    celsius_temperatures = convert_to_celsius(sample_temperatures)
    print(celsius_temperatures)