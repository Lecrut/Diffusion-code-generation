class NumberComparer:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def greater(self):
        return (self.a + self.b + abs(self.a - self.b)) // 2

if __name__ == '__main__':
    comparer = NumberComparer(100, 50)
    print(comparer.greater())