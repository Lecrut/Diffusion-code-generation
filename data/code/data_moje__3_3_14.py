def filter_above_freezing(temperatures):
    return [t for t in temperatures if t >= 0]

if __name__ == '__main__':
    sample_temps = [-5, -1, 0, 3, 10, -2, 25]
    result = filter_above_freezing(sample_temps)
    print(result)