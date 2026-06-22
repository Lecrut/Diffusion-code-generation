def filter_above_freezing(temperatures):
    threshold = {'freezing': 0}
    return [temp for temp in temperatures if temp >= threshold['freezing']]

if __name__ == '__main__':
    sample_temperatures = [-10, -3, 0, 2, 8, 15, -7]
    filtered_temperatures = filter_above_freezing(sample_temperatures)
    print(filtered_temperatures)