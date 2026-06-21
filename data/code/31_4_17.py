class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

if __name__ == '__main__':
    s = Square(4)
    print(s.area())
    s2 = Square(7)
    print(s2.area())