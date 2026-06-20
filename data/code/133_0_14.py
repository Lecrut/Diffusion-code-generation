class IntegerComparator:
    @staticmethod
    def compare(a, b):
        return a == b

if __name__ == '__main__':
    result = IntegerComparator.compare(10, 10)
    print(result)  # True