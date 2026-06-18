def filter_temperatures(temperatures):
    """
    Filters out temperature readings below freezing (0°C).

    Args:
        temperatures (list of float or int): A list containing temperature values.

    Returns:
        list of float or int: A new list with only the temperatures at or above 0°C.
    """
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    # Hard-coded sample data representing temperature readings (in Celsius)
    raw_readings = [-5, -2, 1, 3.5, 0, -8, 7, 4.2, -1.5, 9]

    filtered_data = filter_temperatures(raw_readings)

    print("Filtered temperature readings (>= 0°C):")
    for temp in filtered_data:
        print(f"{temp}°C")