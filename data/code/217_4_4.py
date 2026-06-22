class NumberComparator:
    def compare(self, a, b):
        return f"a {'>' if a > b else '<'} b" if a != b else "a == b"

if __name__ == '__main__':
    comparator = NumberComparator()
    print(comparator.compare(5, 3))
    print(comparator.compare(2, 4))
    print(comparator.compare(7, 7))