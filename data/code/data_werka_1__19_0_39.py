class ComparisonUtility:
    @staticmethod
    def is_greater(a, b):
        return a > b

if __name__ == '__main__':
    result = ComparisonUtility.is_greater(10, 5)
    print(result)