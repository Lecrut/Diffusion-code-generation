class Comparator:
    def check_equality(self, a, b):
        return a == b

if __name__ == '__main__':
    comparator = Comparator()
    result = comparator.check_equality(10, 10)
    print(result)