class EvenValueSum:
    @staticmethod
    def is_even(number):
        return isinstance(number, int) and number % 2 == 0

    @staticmethod
    def sum_even_values(input_dict):
        total = 0
        for value in input_dict.values():
            if EvenValueSum.is_even(value):
                total += value
        return total

if __name__ == '__main__':
    sample_dict = {1: 2, 3: 4, 5: 'a', 6: 7.8, 8: 10}
    result = EvenValueSum.sum_even_values(sample_dict)
    print(result)