def filter_fruits(fruit_color_pairs):
    if not all(isinstance(pair, tuple) and len(pair) == 2 for pair in fruit_color_pairs):
        raise ValueError("Invalid input: each item must be a tuple of two elements")
    
    return [(fruit, color) for fruit, color in fruit_color_pairs if len(fruit) % 2 == 0]

if __name__ == '__main__':
    sample_pairs = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("cherry", "red"),
        ("date", "brown"),
        ("elderberry", "purple")
    ]
    filtered_pairs = filter_fruits(sample_pairs)
    print(filtered_pairs)