class SignChecker:
    POSITIVE = "positive"
    NEGATIVE = "negative"
    ZERO = "zero"

    @staticmethod
    def determine_sign(number):
        if isinstance(number, (int, float)):
            if number > 0:
                return SignChecker.POSITIVE
            if number < 0:
                return SignChecker.NEGATIVE
            return SignChecker.ZERO
        raise ValueError("Input must be a numeric type")

if __name__ == '__main__':
    sample_values = [15, -22, 0, 3.14, -1.5]
    for val in sample_values:
        print(f"{val}: {SignChecker.determine_sign(val)}")