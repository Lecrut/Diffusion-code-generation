class ThreeNumber:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def find_middle(self):
        if self.a > self.b:
            if self.b > self.c:
                return self.b
            else:
                return self.c
        else:
            if self.a < self.b:
                if self.a > self.c:
                    return self.a
                else:
                    return self.c
            else:
                return self.a
if __name__ == '__main__':
    obj = ThreeNumber(10, 5, 20)
    print(obj.find_middle())
    obj2 = ThreeNumber(3, 7, 1)
    print(obj2.find_middle())
    obj3 = ThreeNumber(50, 25, 40)
    print(obj3.find_middle())
    obj4 = ThreeNumber(1, 2, 3)
    print(obj4.find_middle())