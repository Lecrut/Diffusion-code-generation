class MaxFinder:
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def get_max(self):
        return self.v1 if self.v1 >= self.v2 and self.v1 >= self.v3 else (self.v2 if self.v2 >= self.v3 else self.v3)

    def get_values(self):
        return self.v1, self.v2, self.v3

if __name__ == '__main__':
    a = 8
    b = 42
    c = 19
    finder = MaxFinder(a, b, c)
    values = finder.get_values()
    largest = finder.get_max()
    print(values)
    print(largest)