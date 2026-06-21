def compute_area(side_length):
    if side_length < 0:
        raise ValueError("Side length must be non-negative")
    return side_length ** 2

if __name__ == '__main__':
    sample_sides = [5, 10, 0, -3]
    for s in sample_sides:
        try:
            result = compute_area(s)
            print(f"Area for side {s}: {result}")
        except ValueError as e:
            print(f"Error for side {s}: {e}")