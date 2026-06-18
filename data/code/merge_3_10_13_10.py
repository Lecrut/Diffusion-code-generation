def parse_temperature(value: str) -> float | None:
    """Parse a temperature string to a float, returning None if invalid."""
    try:
        return float(value.strip())
    except ValueError:
        return None

if __name__ == '__main__':
    temp1_str = "23.5"
    temp2_str = "-5.0"

    temperature_1 = parse_temperature(temp1_str)
    temperature_2 = parse_temperature(temp2_str)

    if not (temperature_1 is None and temperature_2 is None):
        result = ""
        comparison_signs = [">", "<=", ">="]

        for sign in comparison_signs:
            result += f"{temp1_str} {sign} {temp2_str}: "
            
            if not (temperature_1 is None or temperature_2 is None):
                if temp1 < temp2:
                    result += False + "\n"
                elif temp1 > temp2:
                    result += True + "\n"

        print(result)
    else:
        raise ValueError("Invalid input values")