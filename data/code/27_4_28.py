class Comparator:

    @classmethod
    def are_unequal(cls, first, second):
        return first != second
if __name__ == '__main__':
    result = Comparator.are_unequal(10, 20)
    print(result)
    result = Comparator.are_unequal('hello', 'hello')
    print(result)
    result = Comparator.are_unequal([1, 2, 3], [4, 5, 6])
    print(result)