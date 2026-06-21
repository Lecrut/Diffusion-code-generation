class FruitFilter:
    def __init__(self, fruit_color_pairs):
        self.pairs = fruit_color_pairs

    def filter_even_length_fruits(self):
        return [(fruit, color) for fruit, color in self.pairs if len(fruit) % 2 == 0]

if __name__ == '__main__':
    sample_pairs = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("cherry", "red"),
        ("date", "brown"),
        ("elderberry", "purple")
    ]
    filter_instance = FruitFilter(sample_pairs)
    filtered_pairs = filter_instance.filter_even_length_fruits()
    print(filtered_pairs)