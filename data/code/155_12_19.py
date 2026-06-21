class SumCalculator:
    def __init__(self):
        self.total_sum = 0

    def add_number(self, number):
        if isinstance(number, (int, float)):
            self.total_sum += number
        else:
            raise ValueError("Invalid input type. Only integers and floats are allowed.")

    def get_total_sum(self):
        return self.total_sum

if __name__ == '__main__':
    calculator = SumCalculator()
    sample_values = [10, 20, 35, 42]
    for value in sample_values:
        try:
            calculator.add_number(value)
        except ValueError as e:
            print(e)

    total = calculator.get_total_sum()
    print(f"The total sum is: {total}")