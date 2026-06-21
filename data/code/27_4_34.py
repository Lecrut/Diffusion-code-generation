class Comparator:

    @classmethod
    def are_unequal(cls, arg1, arg2):
        return arg1 != arg2
if __name__ == '__main__':
    result = Comparator.are_unequal(5, 10)
    print(result)
    result = Comparator.are_unequal('hello', 'world')
    print(result)
    result = Comparator.are_unequal(3.14, 3.14)
    print(result)