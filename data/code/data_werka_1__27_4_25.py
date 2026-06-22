class Comparator:
    @classmethod
    def are_unequal(cls, a, b):
        return a != b

if __name__ == '__main__':
    result = Comparator.are_unequal(5, 10)
    print(result)