class MinFinder:
    @staticmethod
    def find_min(items):
        if not items:
            raise ValueError("The iterable cannot be empty")
        return min(items)

if __name__ == '__main__':
    sample_items = [15, 3, 8, 22, 1]
    minimum_value = MinFinder.find_min(sample_items)
    print(minimum_value)