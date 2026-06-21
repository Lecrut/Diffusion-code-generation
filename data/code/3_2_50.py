def filter_above_freezing(temperatures):
    freezing_point = 0
    return [temp for temp in temperatures if temp >= freezing_point]

if __name__ == '__main__':
    sample_temperatures = [-15, -3, 2, 7, 0, -9, 6]
    filtered_temperatures = filter_above_freezing(sample_temperatures)
    print(filtered_temperatures)