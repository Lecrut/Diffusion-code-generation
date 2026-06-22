def filter_above_freezing(temperatures):
    freezing_point = 0
    return [temp for temp in temperatures if temp >= freezing_point]

if __name__ == '__main__':
    sample_temperatures = [-1, 2, -3, 4, 0, -5, 6]
    filtered_temperatures = filter_above_freezing(sample_temperatures)
    print(filtered_temperatures)