def convert_to_celsius(fahrenheit):
    return tuple(map(lambda f: (f - 32) * 5/9, fahrenheit))

if __name__ == '__main__':
    sample_temperatures = (32, 68, 100)
    converted_temperatures = convert_to_celsius(sample_temperatures)
    print(converted_temperatures)