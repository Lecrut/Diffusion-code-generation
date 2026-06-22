class FloatComparison:
    @staticmethod
    def compare_greater(num1, num2):
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise ValueError("Both inputs must be numbers.")
        return num1 > num2

if __name__ == '__main__':
    sample_num1 = 3.14159
    sample_num2 = 2.71828
    result = FloatComparison.compare_greater(sample_num1, sample_num2)
    print(result)