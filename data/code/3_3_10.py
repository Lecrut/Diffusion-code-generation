def filter_freezing_readings(temperatures):
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    sample_readings = [-5, 0, 10, 25, -2, 30]
    result = filter_freezing_readings(sample_readings)
    print(result)