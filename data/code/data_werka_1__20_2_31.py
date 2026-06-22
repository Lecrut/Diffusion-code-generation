class Comparator:

    def check_equality(self, a, b):
        return a == b
if __name__ == '__main__':
    comp = Comparator()
    result = comp.check_equality(5, 5)
    print(result)
    result = comp.check_equality('hello', 'world')
    print(result)
    result = comp.check_equality([1, 2, 3], [1, 2, 3])
    print(result)
    result = comp.check_equality({'a': 1}, {'a': 1})
    print(result)