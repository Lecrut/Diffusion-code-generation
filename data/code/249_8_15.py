class TupleComparator:
    MAX_INT = float('inf')
    MIN_STR = ''

    @staticmethod
    def compare(a, b):
        if isinstance(a, str) and isinstance(b, str):
            return (a > b) - (a < b)
        elif isinstance(a, int) and isinstance(b, int):
            return (a > b) - (a < b)
        else:
            raise TypeError("Both elements must be either strings or integers")

    @classmethod
    def find_largest(cls, data):
        if not data:
            return None
        largest = data[0]
        for item in data[1:]:
            if cls.compare(item, largest) > 0:
                largest = item
        return largest

if __name__ == '__main__':
    list1 = [10, "apple", 5, "banana", 20]
    print(TupleComparator.find_largest(list1))