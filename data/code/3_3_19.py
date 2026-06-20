def filter_above_freezing(temperatures):
    return [t for t in temperatures if t >= 0]

if __name__ == '__main__':
    sample_temps = [23.5, -5.2, 0.0, 30.1, -1.0, 15.8, -10.5, 8.3]
    result = filter_above_freezing(sample_temps)
    print(result)