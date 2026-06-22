class ItemCounter:
    def __init__(self):
        self.num_items = 10

    @staticmethod
    def count_items(num_items):
        total_count = 0
        for i in range(num_items):
            total_count += 1
        return total_count

if __name__ == '__main__':
    counter = ItemCounter()
    print(f"The number of items is: {counter.num_items}")
    print(f"Counted items using function: {ItemCounter.count_items(counter.num_items)}")