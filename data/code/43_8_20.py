class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

if __name__ == '__main__':
    s = Square(5)
    print(s.area())
    s2 = Square(3.5)
    print(s2.area())