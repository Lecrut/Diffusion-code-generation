def filter_above_freezing(temperatures):
    return [t for t in temperatures if t >= 0]

if __name__ == '__main__':
    sample_temperatures = [-5, -1, 0, 3, 10, -2, 7, 15, -3, 22]
    result = filter_above_freezing(sample_temperatures)
    print(result)