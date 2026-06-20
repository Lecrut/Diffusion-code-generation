def filter_freezing_temperatures(readings):
    return [t for t in readings if t >= 0]

if __name__ == '__main__':
    sample_readings = [10.5, -3.2, 0.0, 15.7, -10.1, 25.3, -0.5, 0.1]
    result = filter_freezing_temperatures(sample_readings)
    print(result)