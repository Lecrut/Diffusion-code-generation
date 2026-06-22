def filter_above_freezing(temperatures):
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    sample_temps = [-5, -2, 0, 5, 10, -1, 15, 20]
    result = filter_above_freezing(sample_temps)
    print(result)