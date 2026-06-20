def filter_above_freezing(temperatures):
    return [t for t in temperatures if t >= 0]

if __name__ == '__main__':
    sample_temps = [25.5, -5.0, 0.0, 10.0, -2.3, 100.0]
    result = filter_above_freezing(sample_temps)
    print(result)