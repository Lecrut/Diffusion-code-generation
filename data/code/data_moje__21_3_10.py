class NumberComparator:
    def __init__(self, val_a, val_b, val_c):
        if not all(isinstance(x, (int, float)) for x in (val_a, val_b, val_c)):
            raise TypeError("All inputs must be numeric")
        self.val_a = val_a
        self.val_b = val_b
        self.val_c = val_c

    def get_largest(self):
        max_val = self.val_a
        if self.val_b > max_val:
            max_val = self.val_b
        if self.val_c > max_val:
            max_val = self.val_c
        return max_val

if __name__ == '__main__':
    comparator = NumberComparator(12.5, 8.9, 15.2)
    print(comparator.get_largest())