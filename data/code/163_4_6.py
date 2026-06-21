def filter_fruits(fruit_color_pairs):
    return [(fruit, color) for fruit, color in fruit_color_pairs if len(fruit) % 2 == 0]

if __name__ == '__main__':
    sample_pairs = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("cherry", "red"),
        ("date", "brown")
    ]
    filtered_pairs = filter_fruits(sample_pairs)
    print(filtered_pairs)