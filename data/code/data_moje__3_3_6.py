def filter_above_freezing(temperatures):
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    sample_temperatures = [23, -5, 12, 0, -1, 34, -10, 15]
    result = filter_above_freezing(sample_temperatures)
    print(result)