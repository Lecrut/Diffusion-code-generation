class BooleanComparator:
    @staticmethod
    def compare(a, b):
        return a == b

if __name__ == '__main__':
    result1 = BooleanComparator.compare(True, True)
    result2 = BooleanComparator.compare(False, False)
    print(result1 and result2)