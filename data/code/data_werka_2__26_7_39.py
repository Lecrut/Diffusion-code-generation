class Comparison:
    @staticmethod
    def is_greater(x, y):
        return x > y

if __name__ == '__main__':
    result1 = Comparison.is_greater(5, 3)
    result2 = Comparison.is_greater(7, 10)
    print(result1)
    print(result2)