def filter_temperatures(temperatures):
    return [t for t in temperatures if t >= 0]

if __name__ == '__main__':
    sample_temps = [-5, -1, 0, 5, 10, -10, 15]
    result = filter_temperatures(sample_temps)
    print(result)