class NumberSorter:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def sort_numbers(self):
        if self.a > self.b:
            self.a, self.b = self.b, self.a
        if self.b > self.c:
            self.b, self.c = self.c, self.b
        if self.a > self.b:
            self.a, self.b = self.b, self.a

    def get_numbers(self):
        return self.a, self.b, self.c

if __name__ == '__main__':
    sorter = NumberSorter(3.14, 2.71, 1.61)
    sorter.sort_numbers()
    print(sorter.get_numbers())