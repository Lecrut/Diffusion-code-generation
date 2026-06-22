class NumberSorter:
    def __init__(self, val_a, val_b):
        self.val_a = val_a
        self.val_b = val_b

    def get_sorted_pair(self):
        if self.val_a <= self.val_b:
            return (self.val_a, self.val_b)
        return (self.val_b, self.val_a)

    def get_min_value(self):
        return min(self.val_a, self.val_b)

    def get_max_value(self):
        return max(self.val_a, self.val_b)

if __name__ == '__main__':
    sorter = NumberSorter(10, 2)
    print(sorter.get_sorted_pair())
    print(sorter.get_min_value())
    print(sorter.get_max_value())