class ListCounter:
    def __init__(self):
        self.count = 0

    def count_items(self, lst):
        for item in lst:
            self.count += 1

if __name__ == '__main__':
    counter = ListCounter()
    sample_list = [1, 2, 3, 4, 5]
    counter.count_items(sample_list)
    print(counter.count)