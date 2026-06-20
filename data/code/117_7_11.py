class NumberOperations:
    @staticmethod
    def subtract_numbers(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return float(a - b)
        else:
            raise ValueError('Both inputs must be numbers')

if __name__ == '__main__':
    result = NumberOperations.subtract_numbers(10.5, 3.2)
    print(result)