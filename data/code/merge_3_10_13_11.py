def parse_temperature(value: str) -> float | None:
    """Parse a string to a float, returning None if invalid."""
    try:
        return float(value.strip())
    except ValueError:
        return None

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    temp_a_str = "23.5"
    temp_b_str = "-10.0"

    temperature_a = parse_temperature(temp_a_str)
    temperature_b = parse_temperature(temp_b_str)

    if temperature_a is None or temperature_b is None:
        print("Error: One or both values are not numeric.")
    else:
        comparison_result = ""
        
        if temperature_a > temperature_b:
            comparison_result = f"{temperature_a}°C is greater than {temperature_b}°C"
        elif temperature_a < temperature_b:
            comparison_result = f"{temperature_a}°C is less than {temperature_b}°C"
        else:
            comparison_result = f"{temperature_a}°C equals {temperature_b}°C"

        print(comparison_result)