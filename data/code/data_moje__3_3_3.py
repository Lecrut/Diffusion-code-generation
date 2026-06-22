def filter_above_freezing(temperatures):
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    sample_readings = [-5, -10, 0, 2, 15, -3, 100, 32, -1, 0.5]
    result = filter_above_freezing(sample_readings)
    print(result)