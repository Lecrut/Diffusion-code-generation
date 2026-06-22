class FloatSorter:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sorted(self):
        return (min(self.a, self.b), max(self.a, self.b))

    def get_min(self):
        return min(self.a, self.b)

    def get_max(self):
        return max(self.a, self.b)

if __name__ == '__main__':
    sorter = FloatSorter(5.5, 2.2)
    sorted_values = sorter.get_sorted()
    print(sorted_values)
    print(sorter.get_min())
    print(sorter.get_max())