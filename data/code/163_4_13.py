class FruitFilter:
    EVEN_LENGTH = 2

    @staticmethod
    def is_even_length(fruit):
        return len(fruit) % FruitFilter.EVEN_LENGTH == 0

    def filter_fruits(self, fruit_color_pairs):
        return [(fruit, color) for fruit, color in fruit_color_pairs if self.is_even_length(fruit)]

if __name__ == '__main__':
    sample_pairs = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("cherry", "red"),
        ("date", "brown"),
        ("elderberry", "purple")
    ]
    filter_instance = FruitFilter()
    filtered_pairs = filter_instance.filter_fruits(sample_pairs)
    print(filtered_pairs)