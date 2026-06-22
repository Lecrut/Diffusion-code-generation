class IntegerComparator:
    @staticmethod
    def compare(a, b):
        if a > b:
            return "greater than"
        elif a < b:
            return "less than"
        else:
            return "equal to"

if __name__ == '__main__':
    result = IntegerComparator.compare(10, 5)
    print(result)