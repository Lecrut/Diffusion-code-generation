class NegativeChecker:
    @staticmethod
    def is_negative(number):
        return number < 0

if __name__ == '__main__':
    checker = NegativeChecker()
    sample_number = -15
    print(f"The sample number is: {sample_number}")
    print(f"Is the sample number negative? {checker.is_negative(sample_number)}")