class IntegerComparator:
    @staticmethod
    def compare(a: int, b: int) -> bool:
        return a == b

if __name__ == '__main__':
    print(IntegerComparator.compare(5, 5))  # True
    print(IntegerComparator.compare(3, 4))  # False