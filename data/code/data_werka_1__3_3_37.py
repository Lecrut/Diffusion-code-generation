def filter_temperatures_above_freezing(temperatures):
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    sample_temperatures = [-5, 3, -1, 15, 0, -20, 10]
    filtered_temperatures = filter_temperatures_above_freezing(sample_temperatures)
    print(filtered_temperatures)