def _to_digit_list(number: int) -> list[int]:
    if number < 0:
        raise ValueError("Input must be a positive integer")
    return [int(char) for char in str(number)]

def sum_of_digits(number: int) -> int:
    digits = _to_digit_list(number)
    return sum(digits)

class SumCalculator:
    def __init__(self):
        self._cache = 0

    def compute(self, number: int) -> int:
        self._cache = sum_of_digits(number)
        return self._cache

    def get_cache(self) -> int:
        return self._cache

if __name__ == '__main__':
    test_value_1 = 12345
    print(sum_of_digits(test_value_1))
    test_value_2 = 987654321
    print(sum_of_digits(test_value_2))
    calc = SumCalculator()
    print(calc.compute(55555))
    print(calc.get_cache())