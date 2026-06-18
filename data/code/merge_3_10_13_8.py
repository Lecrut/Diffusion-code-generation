def parse_temperature(value: str) -> float | None:
    """Parse a temperature string into a float, returning None if invalid."""
    try:
        return float(value.strip())
    except ValueError:
        return None

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    temp_a = "23.5"
    temp_b = "-10.0"

    val_a = parse_temperature(temp_a)
    val_b = parse_temperature(temp_b)

    if val_a is None or val_b is None:
        print("Error: One or both temperature values are not numeric.")
    else:
        comparison_msg = ""
        if val_a < val_b:
            comparison_msg = f"{val_a}°C is lower than {val_b}°C"
        elif val_a > val_b:
            comparison_msg = f"{val_a}°C is higher than {val_b}°C"
        else:
            comparison_msg = f"{val_a}°C equals {val_b}°C"

        print(comparison_msg)