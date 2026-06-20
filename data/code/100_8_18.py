class NumberComparison:
    @staticmethod
    def check_sum_greater_than_difference(num1, num2):
        return (num1 + num2) > abs(num1 - num2)

if __name__ == '__main__':
    val_a = 10
    val_b = 5
    final_outcome = NumberComparison.check_sum_greater_than_difference(val_a, val_b)
    print(final_outcome)