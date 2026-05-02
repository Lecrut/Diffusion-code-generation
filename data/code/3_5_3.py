def filter_temperatures(readings):
    filtered_temps = [temp for temp in readings if temp >= 0]
    return filtered_temps
if __name__ == '__main__':
    sample_readings = [10, -5, 2, 0, -10, 15, 0, 30, -2, 5]
    result = filter_temperatures(sample_readings)
    print(result)