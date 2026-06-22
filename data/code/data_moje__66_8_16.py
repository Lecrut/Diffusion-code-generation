def kilometers_to_meters(kilometers):
    if not isinstance(kilometers, (int, float)):
        raise ValueError("Input must be a number.")
    if kilometers < 0:
        raise ValueError("Input must be non-negative.")
    return kilometers * 1000

if __name__ == '__main__':
    sample_values = [5, 0, 10.5, -1, "invalid"]
    
    for val in sample_values:
        try:
            result = kilometers_to_meters(val)
            print(f"{val} km = {result} m")
        except ValueError as e:
            print(f"Error for {val}: {e}")