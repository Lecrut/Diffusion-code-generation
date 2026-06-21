class BooleanComparator:
    @staticmethod
    def compare(a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    result = BooleanComparator.compare(True, False)
    print(result)