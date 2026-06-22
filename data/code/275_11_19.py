class EvenSumCalculator:
    @staticmethod
    def is_even(number):
        return isinstance(number, int) and number % 2 == 0

    @classmethod
    def sum_even_values(cls, input_dict):
        total = 0
        for value in input_dict.values():
            if cls.is_even(value):
                total += value
        return total

if __name__ == '__main__':
    sample_dict = {1: 2, 3: 4, 5: 'a', 6: 7.8, 8: 10}
    calculator = EvenSumCalculator()
    result = calculator.sum_even_values(sample_dict)
    print(result)