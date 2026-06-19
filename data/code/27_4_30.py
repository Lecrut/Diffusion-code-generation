class Comparator:

    @staticmethod
    def are_unequal(value1, value2):
        return value1 != value2
if __name__ == '__main__':
    result = Comparator.are_unequal(10, 20)
    print(result)
    result = Comparator.are_unequal('hello', 'hello')
    print(result)