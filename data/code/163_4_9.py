def filter_even_length_fruits(fruit_color_pairs):
    if not all(isinstance(pair, tuple) and len(pair) == 2 for pair in fruit_color_pairs):
        raise ValueError("Input must be a list of (fruit, color) tuples")
    return [(fruit, color) for fruit, color in fruit_color_pairs if len(fruit) % 2 == 0]

if __name__ == '__main__':
    sample_pairs = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("cherry", "red"),
        ("date", "brown"),
        ("elderberry", "purple")
    ]
    try:
        filtered_pairs = filter_even_length_fruits(sample_pairs)
        print(filtered_pairs)
    except ValueError as e:
        print(e)