def filter_temperatures(temperatures):
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    sample_temperatures = [-5, 3, -1, 12, 0, -8, 7]
    filtered_temperatures = filter_temperatures(sample_temperatures)
    print(filtered_temperatures)