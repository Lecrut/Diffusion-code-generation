class ListCounter:
    def __init__(self):
        self.count = 0

    @staticmethod
    def count_items(lst):
        counter = ListCounter()
        for _ in lst:
            counter.add_item()
        return counter.get_count()

    def add_item(self):
        self.count += 1

    def get_count(self):
        return self.count

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(ListCounter.count_items(sample_list))