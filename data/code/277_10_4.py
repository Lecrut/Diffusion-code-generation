class ItemCounter:
    def __init__(self):
        self.count = 0

    def add_item(self, item):
        self.count += 1

    def get_count(self):
        return self.count

if __name__ == '__main__':
    counter = ItemCounter()
    sample_list = [1, 2, 3, 4, 5]
    for item in sample_list:
        counter.add_item(item)
    print(counter.get_count())