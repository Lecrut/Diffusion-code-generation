class MinFinder:
    @staticmethod
    def find_minimum(items):
        if not items:
            raise ValueError("The iterable cannot be empty")
        return min(items)

if __name__ == '__main__':
    sample_items = [15, 3, 8, 22, 1]
    minimum_value = MinFinder.find_minimum(sample_items)
    print(minimum_value)