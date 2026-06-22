def filter_non_freezing_temperatures(temperatures):
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    sample_temperatures = [-5, 3, -1, 15, 0, -20, 10]
    filtered_temperatures = filter_non_freezing_temperatures(sample_temperatures)
    print(filtered_temperatures)