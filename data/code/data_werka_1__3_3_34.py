def filter_temperatures(temperatures):
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    sample_temperatures = [-10, -5, 0, 5, 10, 15, -3, 2]
    filtered_temperatures = filter_temperatures(sample_temperatures)
    print(filtered_temperatures)