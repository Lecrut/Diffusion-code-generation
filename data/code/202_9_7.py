class MaxFinder:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def find_max(self):
        if self.a >= self.b and self.a >= self.c:
            return self.a
        elif self.b >= self.a and self.b >= self.c:
            return self.b
        else:
            return self.c

if __name__ == '__main__':
    finder = MaxFinder(10, 20, 30)
    max_val = finder.find_max()
    print(max_val)