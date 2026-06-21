def filter_fruits(fruit_color_pairs):
    return [(fruit, color) for fruit, color in fruit_color_pairs if len(fruit) % 2 == 0]

if __name__ == '__main__':
    sample_pairs = [
        ("strawberry", "red"),
        ("mango", "yellow"),
        ("blueberry", "blue"),
        ("raspberry", "red"),
        ("pineapple", "green")
    ]
    filtered_pairs = filter_fruits(sample_pairs)
    print(filtered_pairs)