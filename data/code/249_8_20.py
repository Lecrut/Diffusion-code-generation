class LargestItemFinder:
    @staticmethod
    def compare_items(a, b):
        if isinstance(a, str) and isinstance(b, str):
            return (a > b) - (a < b)
        elif isinstance(a, int) and isinstance(b, int):
            return (a > b) - (a < b)
        else:
            raise TypeError("Items must be either both strings or both integers")

    @staticmethod
    def find_largest(data):
        if not data:
            return None
        largest = data[0]
        for item in data[1:]:
            comparison_result = LargestItemFinder.compare_items(largest, item)
            if comparison_result < 0:
                largest = item
        return largest

if __name__ == '__main__':
    list1 = [10, "apple", 5, "banana", 20]
    finder = LargestItemFinder()
    print(finder.find_largest(list1))