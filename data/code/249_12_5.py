class MaxFinder:
    def __init__(self):
        self.max_item = None

    def find_largest(self, items: list) -> int:
        if not items:
            raise ValueError("List is empty")
        self.max_item = items[0]
        for item in items[1:]:
            if item > self.max_item:
                self.max_item = item
        return self.max_item

if __name__ == '__main__':
    finder = MaxFinder()
    sample_list = [3, 5, 1, 2, 4]
    print(finder.find_largest(sample_list))