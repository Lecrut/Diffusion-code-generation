def filter_above_freezing(temperatures):
    if not isinstance(temperatures, list):
        raise ValueError("Input must be a list")
    if any(not isinstance(temp, (int, float)) for temp in temperatures):
        raise ValueError("All elements in the list must be numbers")
    
    freezing_point = 0
    return [temp for temp in temperatures if temp >= freezing_point]

if __name__ == '__main__':
    sample_temperatures = [-10, 0, 5, -3, 12, -8, 7]
    try:
        filtered_temperatures = filter_above_freezing(sample_temperatures)
        print(filtered_temperatures)
    except ValueError as e:
        print(e)