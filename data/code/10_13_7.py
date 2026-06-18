def parse_temperature(value: str) -> float | None:
    """Attempt to convert a string to a float."""
    try:
        return float(value.strip())
    except ValueError:
        return None

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    temp_a = "25"
    temp_b = "-10"

    val_a = parse_temperature(temp_a)
    val_b = parse_temperature(temp_b)

    if val_a is None or val_b is None:
        print("Error: Invalid temperature value provided.")
    else:
        comparison_result = ""
        if val_a > val_b:
            result_str = "A"
            comparison_result = f"{temp_a}°C ({val_a}) is greater than {temp_b}°C ({val_b})."
        elif val_a < val_b:
            result_str = "B"
            comparison_result = f"{temp_b}°C ({val_b}) is greater than {temp_a}°C ({val_a})."
        else:
            result_str = "="
            comparison_result = f"{temp_a}°C ({val_a}) equals {temp_b}°C ({val_b})."

        print(f"Comparison [{result_str}]")
        print(comparison_result)