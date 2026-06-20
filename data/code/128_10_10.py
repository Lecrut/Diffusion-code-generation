class NumberChecker:
    def is_negative(self, number):
        return number < 0

if __name__ == '__main__':
    checker = NumberChecker()
    sample_number1 = -15
    print(f"The sample number {sample_number1} is negative: {checker.is_negative(sample_number1)}")
    sample_number2 = 42
    print(f"The sample number {sample_number2} is negative: {checker.is_negative(sample_number2)}")
    sample_number3 = 0
    print(f"The sample number {sample_number3} is negative: {checker.is_negative(sample_number3)}")