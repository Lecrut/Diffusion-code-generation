def is_negative(value):
    if isinstance(value, (int, float)):
        return value < 0
    raise ValueError("Unsupported input type")

if __name__ == '__main__':
    sample_values = [10, -5, 3.14, -2.71, "string", None]
    for val in sample_values:
        try:
            print(f"{val}: {is_negative(val)}")
        except ValueError as e:
            print(f"{val}: {e}")