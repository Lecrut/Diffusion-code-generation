class Comparator:

    @classmethod
    def are_unequal(cls, arg1, arg2):
        return arg1 != arg2
if __name__ == '__main__':
    result = Comparator.are_unequal(5, 10)
    print(result)
    result = Comparator.are_unequal('hello', 'hello')
    print(result)
    result = Comparator.are_unequal([1, 2, 3], [1, 2, 3])
    print(result)
    result = Comparator.are_unequal({'a': 1}, {'a': 1})
    print(result)