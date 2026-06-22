class NumberComparer:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compare(self):
        return f"a {'>=' if self.a >= self.b else '<'} b"

if __name__ == '__main__':
    comparer1 = NumberComparer(5, 3)
    print(comparer1.compare())

    comparer2 = NumberComparer(2, 4)
    print(comparer2.compare())

    comparer3 = NumberComparer(7, 7)
    print(comparer3.compare())