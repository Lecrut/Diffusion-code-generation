def filter_temperatures(readings):
    filtered_temps = [temp for temp in readings if temp >= 0]
    return filtered_temps
if __name__ == '__main__':
    sample_readings = [10.5, -5.2, 32.0, 0.0, -1.0, 15.7, -22.5, 25.1]
    result = filter_temperatures(sample_readings)
    print(result)