class GreaterFinder:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def find_greater(self):
        diff = self.a - self.b
        abs_diff = (diff + abs(diff)) // 2
        return self.b + abs_diff

if __name__ == '__main__':
    finder = GreaterFinder(35, 40)
    print(finder.find_greater())