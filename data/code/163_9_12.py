class FruitColorMerger:
    DEFAULT_FRUITS = ["apple", "banana", "grape", "orange"]
    DEFAULT_COLORS = ["red", "yellow", "purple", "orange"]

    @staticmethod
    def merge_fruit_color_pairs(fruits=DEFAULT_FRUITS, colors=DEFAULT_COLORS):
        return {fruit: color for fruit, color in zip(fruits, colors)}

if __name__ == '__main__':
    merger = FruitColorMerger()
    merged_dict = merger.merge_fruit_color_pairs()
    print(merged_dict)