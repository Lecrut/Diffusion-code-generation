def filter_above_freezing(temperatures):
    if not isinstance(temperatures, list):
        raise ValueError("Input must be a list")
    return [temp for temp in temperatures if isinstance(temp, (int, float)) and temp >= 0]

if __name__ == '__main__':
    sample_temperatures = [-15, -3, 0, 7, 20, -1, 12]
    try:
        filtered_temperatures = filter_above_freezing(sample_temperatures)
        print(filtered_temperatures)
    except ValueError as e:
        print(e)