class FruitFilter:
    @staticmethod
    def is_even_length(fruit):
        return len(fruit) % 2 == 0

    def filter_pairs(self, fruit_color_pairs):
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
    filtered_pairs = filter_instance.filter_pairs(sample_pairs)
    print(filtered_pairs)