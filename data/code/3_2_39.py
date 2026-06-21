def filter_above_freezing(temperatures):
    return list(filter(lambda temp: temp >= 0, temperatures))

if __name__ == '__main__':
    sample_temperatures = [-20, -15, -5, 0, 5, 10, 15]
    filtered_temperatures = filter_above_freezing(sample_temperatures)
    print(filtered_temperatures)