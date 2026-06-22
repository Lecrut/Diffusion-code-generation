class Comparator:

    def check_equality(self, a, b):
        return a == b
if __name__ == '__main__':
    comparator = Comparator()
    result = comparator.check_equality(5, 5)
    print(result)
    result = comparator.check_equality('hello', 'world')
    print(result)
    result = comparator.check_equality([1, 2, 3], [1, 2, 3])
    print(result)
    result = comparator.check_equality({'a': 1}, {'b': 1})
    print(result)