class Comparator:

    @classmethod
    def are_unequal(cls, a, b):
        return a != b
if __name__ == '__main__':
    result = Comparator.are_unequal(5, 10)
    print(result)
    result = Comparator.are_unequal('hello', 'world')
    print(result)
    result = Comparator.are_unequal([1, 2, 3], [1, 2, 3])
    print(result)