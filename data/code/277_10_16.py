class ItemCounter:
    def __init__(self):
        self.count = 0

    def add_item(self, item):
        self.count += 1

def count_items(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    counter = ItemCounter()
    for item in lst:
        counter.add_item(item)
    return counter.get_count()

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(count_items(sample_list))