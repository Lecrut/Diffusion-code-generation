def filter_above_freezing(temperatures):
    return [t for t in temperatures if t >= 0]

if __name__ == '__main__':
    sample_readings = [20.5, -3.2, 0, 15.8, -10, 32, -0.1, 5]
    result = filter_above_freezing(sample_readings)
    print(result)