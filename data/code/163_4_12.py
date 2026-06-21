def filter_fruits(fruit_color_pairs):
    filtered = []
    for fruit, color in fruit_color_pairs:
        if len(fruit) % 2 == 0:
            filtered.append((fruit, color))
    return filtered

if __name__ == '__main__':
    sample_pairs = [
        ("apple", "red"),
        ("peach", "pink"),
        ("strawberry", "red"),
        ("raspberry", "red"),
        ("kiwi", "brown")
    ]
    filtered_pairs = filter_fruits(sample_pairs)
    print(filtered_pairs)