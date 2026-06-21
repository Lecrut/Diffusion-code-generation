def validate_temperatures(temperatures):
    if not isinstance(temperatures, list):
        raise ValueError("Input must be a list of temperatures.")
    for temp in temperatures:
        if not isinstance(temp, (int, float)):
            raise ValueError("All elements in the temperature list must be numbers.")

def filter_above_freezing(temperatures):
    validate_temperatures(temperatures)
    freezing_point = 0
    return [temp for temp in temperatures if temp >= freezing_point]

if __name__ == '__main__':
    sample_temperatures = [-1, 2, -3, 4, 0, -5, 6]
    filtered_temperatures = filter_above_freezing(sample_temperatures)
    print(filtered_temperatures)