FILTER_THRESHOLD = 2

def filter_even_length_fruits(fruit_color_pairs):
    return [(fruit, color) for fruit, color in fruit_color_pairs if len(fruit) % FILTER_THRESHOLD == 0]

if __name__ == '__main__':
    sample_pairs = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("cherry", "red"),
        ("date", "brown"),
        ("elderberry", "purple")
    ]
    filtered_pairs = filter_even_length_fruits(sample_pairs)
    print(filtered_pairs)