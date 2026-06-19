def filter_above_freezing(temperatures):
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    sample_temperatures = [-10, -5, 0, 5, 10, -3, 15]
    filtered_temperatures = filter_above_freezing(sample_temperatures)
    print(filtered_temperatures)