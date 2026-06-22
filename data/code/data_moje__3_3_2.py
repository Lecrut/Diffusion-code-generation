def filter_freezing_readings(temperatures):
    return [t for t in temperatures if t >= 0]

if __name__ == '__main__':
    sample_temperatures = [-5, 0, 10, -2, 25, 3.5, -100]
    result = filter_freezing_readings(sample_temperatures)
    print(result)