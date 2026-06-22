def convert_f_to_c(fahrenheit):
    return list(map(lambda f: (f - 32) * 5.0 / 9.0, fahrenheit))

if __name__ == '__main__':
    sample_temperatures = (32, 68, 100, 212)
    converted_temperatures = convert_f_to_c(sample_temperatures)
    print(converted_temperatures)