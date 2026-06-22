def filter_above_freezing(temperatures):
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    sample_temps = [-5, 0, 10, -2, 25, 3, -10, 100]
    result = filter_above_freezing(sample_temps)
    print(result)