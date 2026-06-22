class MathOperations:
    @staticmethod
    def product_of_tuple(numbers):
        result = 1
        for number in numbers:
            result *= number
        return result

if __name__ == '__main__':
    sample_values = (2, 3, 4)
    print(MathOperations.product_of_tuple(sample_values))