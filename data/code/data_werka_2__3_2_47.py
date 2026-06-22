def filter_above_freezing(temperatures):
    if not isinstance(temperatures, list):
        raise ValueError("Input must be a list of temperatures.")
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    sample_temperatures = [-10, -5, 0, 5, 10, 15, -3]
    try:
        filtered_temperatures = filter_above_freezing(sample_temperatures)
        print(filtered_temperatures)
    except ValueError as e:
        print(e)