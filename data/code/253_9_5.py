class ThreeNumberFinder:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def find_middle(self):
        if (self.a <= self.b <= self.c) or (self.c <= self.b <= self.a):
            return self.b
        elif (self.b <= self.a <= self.c) or (self.c <= self.a <= self.b):
            return self.a
        else:
            return self.c
if __name__ == '__main__':
    num1 = 5
    num2 = 2
    num3 = 8
    finder = ThreeNumberFinder(num1, num2, num3)
    middle_value = finder.find_middle()
    print(middle_value)