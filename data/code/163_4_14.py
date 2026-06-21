MAX_FRUIT_LENGTH = 10

def filter_fruits(fruit_color_pairs):
    return [(fruit, color) for fruit, color in fruit_color_pairs if len(fruit) <= MAX_FRUIT_LENGTH]

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