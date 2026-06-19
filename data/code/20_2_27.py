class Comparator:

    def check_equality(self, a, b):
        return a == b
if __name__ == '__main__':
    comparator = Comparator()
    result1 = comparator.check_equality(5, 5)
    print(result1)
    result2 = comparator.check_equality('hello', 'world')
    print(result2)
    result3 = comparator.check_equality([1, 2, 3], [1, 2, 3])
    print(result3)