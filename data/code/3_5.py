def filter_freezing_temperatures(readings):
    filtered_temperatures = [temp for temp in readings if temp >= 0]
    return filtered_temperatures
if __name__ == '__main__':
    sample_readings = [10, -5, 2, 0, -10, 15, -3, 0, 25, -1]
    result = filter_freezing_temperatures(sample_readings)
    print(result)