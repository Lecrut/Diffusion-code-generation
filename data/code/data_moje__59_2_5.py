def compute_sum_of_digits(value):
    if not isinstance(value, int) or value < 0:
        raise TypeError("Input must be a non-negative integer")
    
    current_sum = 0
    temp = value
    while temp > 0:
        current_sum += temp % 10
        temp //= 10
    return current_sum

class DigitalSumCalculator:
    def __init__(self, number):
        self._number = number

    def get_sum(self):
        if self._number == 0:
            return 0
        return self._number % 10 + DigitalSumCalculator(self._number // 10).get_sum()

if __name__ == '__main__':
    calc1 = DigitalSumCalculator(12345)
    print(calc1.get_sum())
    
    calc2 = DigitalSumCalculator(0)
    print(calc2.get_sum())
    
    result = compute_sum_of_digits(9876543210)
    print(result)