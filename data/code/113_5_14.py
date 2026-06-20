class NumberOperations:
    @staticmethod
    def subtract_numbers(a, b):
        return a - b

if __name__ == '__main__':
    result = NumberOperations.subtract_numbers(10, 5)
    print(result)