class Comparator:

    def check_equality(self, a, b):
        return a == b
if __name__ == '__main__':
    comparator = Comparator()
    result = comparator.check_equality(10, 10)
    print(result)
    result = comparator.check_equality('hello', 'world')
    print(result)
    result = comparator.check_equality([1, 2, 3], [1, 2, 3])
    print(result)