class MaxFinder:

    def __init__(self):
        self.max_item = None

    def add_item(self, item):
        if self.max_item is None or item > self.max_item:
            self.max_item = item

def find_max(items: list) -> int:
    finder = MaxFinder()
    for item in items:
        finder.add_item(item)
    return finder.max_item
if __name__ == '__main__':
    sample_list1 = [3, 5, 1, 2, 4]
    sample_list2 = [7, 7.0, 7.5]
    print(find_max(sample_list1))
    print(find_max(sample_list2))