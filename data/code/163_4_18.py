def filter_fruit_colors(pairs):
    return [(fruit, color) for fruit, color in pairs if len(fruit) % 2 == 0]

if __name__ == '__main__':
    sample_pairs = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("cherry", "red"),
        ("date", "brown"),
        ("elderberry", "purple")
    ]
    filtered_pairs = filter_fruit_colors(sample_pairs)
    print(filtered_pairs)