class Validator:
    def combine_and_report(self, num1, num2, num3):
        is_positive = all(n > 0 for n in [num1, num2, num3])
        is_even = all(n % 2 == 0 for n in [num1, num2, num3])
        is_less_than_100 = all(n < 100 for n in [num1, num2, num3])

        status_report = {
            'number1': num1,
            'number2': num2,
            'number3': num3,
            'is_positive': is_positive,
            'is_even': is_even,
            'is_less_than_100': is_less_than_100
        }

        return status_report

if __name__ == '__main__':
    validator = Validator()
    result = validator.combine_and_report(2, 4, 6)
    print(result)