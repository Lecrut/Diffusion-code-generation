def celsius_to_fahrenheit(celsius_list):
    return [(c * 9 / 5) + 32 for c in celsius_list]

if __name__ == '__main__':
    sample_celsius = [0, 10, 20, 30, 40, 50, 100]
    fahrenheit_results = celsius_to_fahrenheit(sample_celsius)
    print(fahrenheit_results)