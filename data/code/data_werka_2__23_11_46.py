class NumberComparer:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def greater(self):
        return (self.a + self.b + abs(self.a - self.b)) // 2

if __name__ == '__main__':
    comparer1 = NumberComparer(35, 40)
    print(comparer1.greater())

    comparer2 = NumberComparer(100, 85)
    print(comparer2.greater())