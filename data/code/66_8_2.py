def convert_km_to_m(kilometers):
    if not isinstance(kilometers, (int, float)):
        raise ValueError("Input must be a number.")
    if kilometers < 0:
        raise ValueError("Input must be non-negative.")
    return kilometers * 1000

if __name__ == "__main__":
    sample_values = [1, 0, 2.5, 100]
    for value in sample_values:
        result = convert_km_to_m(value)
        print(f"{value} km is {result} m")
    try:
        convert_km_to_m(-5)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        convert_km_to_m("10")
    except ValueError as e:
        print(f"Error: {e}")