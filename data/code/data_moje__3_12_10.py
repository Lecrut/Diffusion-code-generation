def celsius_to_fahrenheit(temperatures):
    return [(t * 9 / 5) + 32 for t in temperatures]

if __name__ == '__main__':
    sample_celsius = [-40, -18, 0, 20, 37, 100]
    result = celsius_to_fahrenheit(sample_celsius)
    print(result)