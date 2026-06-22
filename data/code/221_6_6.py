class ValueSorter:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def sort_values(self):
        min_val = min(self.a, self.b, self.c)
        max_val = max(self.a, self.b, self.c)
        middle_val = self.a + self.b + self.c - min_val - max_val
        return (min_val, middle_val, max_val)

if __name__ == '__main__':
    sorter = ValueSorter(5, 2, 8)
    result = sorter.sort_values()
    print(result)