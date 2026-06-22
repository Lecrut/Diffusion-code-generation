def kilometers_to_meters(km):
    if not isinstance(km, (int, float)):
        raise ValueError("Input must be a number")
    if km < 0:
        raise ValueError("Input must be non-negative")
    return km * 1000

if __name__ == '__main__':
    sample_values = [5, 0, 10.5, -3, "abc"]
    for val in sample_values:
        try:
            result = kilometers_to_meters(val)
            print(f"{val} km = {result} m")
        except ValueError as e:
            print(f"Input {val} caused error: {e}")