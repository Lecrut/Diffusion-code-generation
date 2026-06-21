def celsius_to_fahrenheit(celsius_list):
    return [(c * 9/5) + 32 for c in celsius_list]

if __name__ == '__main__':
    sample_celsius_values = [0, 10, 20, 30, 40]
    converted_values = celsius_to_fahrenheit(sample_celsius_values)
    print(converted_values)