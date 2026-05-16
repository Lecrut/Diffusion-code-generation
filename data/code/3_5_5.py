def filter_temperatures(readings):
    filtered_temps = [temp for temp in readings if temp >= 0]
    return filtered_temps
if __name__ == '__main__':
    sample_readings = [10.5, -5.2, 0.0, 22.1, -1.0, 35.8, -10.5, 0.001]
    result = filter_temperatures(sample_readings)
    print(result)