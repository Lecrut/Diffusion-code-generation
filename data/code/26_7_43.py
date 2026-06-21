class Comparator:
    @staticmethod
    def is_greater(x, y):
        return x > y

if __name__ == '__main__':
    print(Comparator.is_greater(10, 5))
    print(Comparator.is_greater(3, 7))