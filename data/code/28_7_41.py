class ComparisonHelper:

    @staticmethod
    def greater_than(a, b):
        return a > b

def is_larger(a, b):
    return ComparisonHelper.greater_than(a, b)
if __name__ == '__main__':
    print(is_larger(10, 5))
    print(is_larger(3, 7))
    print(is_larger(-1, -2))
    print(is_larger(0, 0))