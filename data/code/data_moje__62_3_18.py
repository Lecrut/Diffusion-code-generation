def calculate_divisors(n):
    if n != 1:
        raise ValueError("Only the number 1 is supported for this task")
    return [1]

class DivisorCalculator:
    def __init__(self, value):
        self.value = value

    def get_divisors(self):
        return calculate_divisors(self.value)

if __name__ == '__main__':
    target_number = 1
    calculator = DivisorCalculator(target_number)
    print(calculator.get_divisors())