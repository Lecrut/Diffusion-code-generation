def filter_above_freezing(temperatures):
    freezing_point = 0
    filtered_temps = []
    for temp in temperatures:
        if temp >= freezing_point:
            filtered_temps.append(temp)
    return filtered_temps

if __name__ == '__main__':
    sample_temperatures = [-2, -1, 0, 3, 8, -7, 4]
    result = filter_above_freezing(sample_temperatures)
    print(result)