class Comparator:

    @staticmethod
    def is_greater(a, b):
        return a > b
if __name__ == '__main__':
    result = Comparator.is_greater(5, 3)
    print(result)
    result = Comparator.is_greater(2, 4)
    print(result)