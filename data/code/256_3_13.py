def find_range(data):
    if not data:
        raise ValueError("Input set cannot be empty")
    return max(data) - min(data)

if __name__ == '__main__':
    sample_sets = [
        {1, 5, 2, 8, 3},
        {10, 4, 7, 1, 9},
        set(),
        {5}
    ]
    for s in sample_sets:
        try:
            print(f"Range of {s}: {find_range(s)}")
        except ValueError as e:
            print(f"Error for {s}: {e}")