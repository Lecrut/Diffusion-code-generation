class NumericOperations:
    @staticmethod
    def validate_number(value):
        if not isinstance(value, (int, float)):
            raise ValueError('Input must be a number')

    @staticmethod
    def subtract_numbers(a, b):
        NumericOperations.validate_number(a)
        NumericOperations.validate_number(b)
        return a - b

if __name__ == '__main__':
    result = NumericOperations.subtract_numbers(10, 5)
    print(result)