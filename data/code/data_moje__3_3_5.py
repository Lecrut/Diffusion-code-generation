def filter_temperatures(temperatures):
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    sample_temperatures = [-5.2, 10.5, 0, 3.8, -1.0, 15.0, 0.0, -20.5]
    result = filter_temperatures(sample_temperatures)
    print(result)