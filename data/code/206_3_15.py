class MinFinder:
    def __init__(self, data):
        if not data:
            raise ValueError("List cannot be empty")
        self.data = data

    def find_min(self):
        min_item = self.data[0]
        for item in self.data[1:]:
            if item < min_item:
                min_item = item
        return min_item

if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3]
    finder = MinFinder(sample_list)
    minimum_value = finder.find_min()
    print(minimum_value)