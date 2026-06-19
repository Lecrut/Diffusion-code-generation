class Comparator:

    @staticmethod
    def are_unequal(arg1, arg2):
        return arg1 != arg2
if __name__ == '__main__':
    result = Comparator.are_unequal(5, 10)
    print(result)
    result = Comparator.are_unequal('hello', 'hello')
    print(result)