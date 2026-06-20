class NumberProperties:
    def __init__(self, number):
        self.number = number

    @staticmethod
    def is_positive(number):
        return number > 0

    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @staticmethod
    def is_less_than_100(number):
        return number < 100

    def combine_checks(self):
        positive = self.is_positive(self.number)
        even = self.is_even(self.number)
        less_than_100 = self.is_less_than_100(self.number)
        if positive and even and less_than_100:
            return "Number is positive, even, and less than 100."
        elif positive and even:
            return "Number is positive and even."
        elif positive and less_than_100:
            return "Number is positive and less than 100."
        elif even and less_than_100:
            return "Number is even and less than 100."
        elif positive:
            return "Number is positive."
        elif even:
            return "Number is even."
        elif less_than_100:
            return "Number is less than 100."
        else:
            return "Number does not meet any criteria."

if __name__ == '__main__':
    test_numbers = [10, -5, 7, 25, 0, 12]
    for num in test_numbers:
        np = NumberProperties(num)
        print(np.combine_checks())