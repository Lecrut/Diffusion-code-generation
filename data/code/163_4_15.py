def filter_even_length_fruits(fruit_color_pairs):
    return [(fruit, color) for fruit, color in fruit_color_pairs if len(fruit) % 2 == 0]

if __name__ == '__main__':
    sample_pairs = [
        ("grape", "green"),
        ("orange", "orange"),
        ("kiwi", "brown"),
        ("mango", "yellow"),
        ("blueberry", "blue")
    ]
    filtered_pairs = filter_even_length_fruits(sample_pairs)
    print(filtered_pairs)