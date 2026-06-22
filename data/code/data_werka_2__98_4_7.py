def categorize_number(value):
    boundaries = [
        (0, 10, 'low'),
        (10, 50, 'medium'),
        (50, float('inf'), 'high')
    ]
    for min_val, max_val, label in boundaries:
        if min_val <= value < max_val:
            return label
    raise ValueError(f"Input {value} does not fit defined ranges")

if __name__ == '__main__':
    print(categorize_number(5))
    print(categorize_number(25))
    print(categorize_number(100))
    print(categorize_number(10))
    print(categorize_number(50))