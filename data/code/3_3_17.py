def filter_freezing(temperatures):
    return [t for t in temperatures if t >= 0]

if __name__ == '__main__':
    sample_temps = [-5, -1, 0, 1, 5, 10, -10, 20]
    result = filter_freezing(sample_temps)
    print(result)