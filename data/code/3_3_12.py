def filter_above_freezing(temperatures):
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    sample_temperatures = [-5, -1, 0, 3, 15, -10, 22, 5, -3]
    result = filter_above_freezing(sample_temperatures)
    print(result)