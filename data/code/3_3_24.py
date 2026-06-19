def filter_above_freezing(temperatures):
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    sample_temperatures = [-10, -5, 0, 3, 7, -2, 8, -1, 4]
    filtered_temperatures = filter_above_freezing(sample_temperatures)
    print(filtered_temperatures)