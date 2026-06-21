class MaxFinder:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def find_max(self):
        return max(self.a, self.b, self.c)

if __name__ == '__main__':
    finder = MaxFinder(10, 20, 30)
    print(finder.find_max())