class Comparator:

    @classmethod
    def are_unequal(cls, a, b):
        return a != b
if __name__ == '__main__':
    result = Comparator.are_unequal(10, 20)
    print(result)
    result = Comparator.are_unequal('hello', 'world')
    print(result)
    result = Comparator.are_unequal(3.14, 3.14)
    print(result)