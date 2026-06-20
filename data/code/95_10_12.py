class Validator:
    def check_positive(self, number):
        return number > 0

    def check_even(self, number):
        return number % 2 == 0

    def check_magnitude(self, number):
        return number < 100

    def combine_and_report(self, num1, num2, num3):
        report = {
            'num1': num1,
            'num2': num2,
            'num3': num3
        }
        status = []
        
        if self.check_positive(num1) and self.check_even(num1) and self.check_magnitude(num1):
            status.append('Positive, Even, Less than 100')
        else:
            status.append('Does not meet all criteria')

        if self.check_positive(num2) and self.check_even(num2) and self.check_magnitude(num2):
            status.append('Positive, Even, Less than 100')
        else:
            status.append('Does not meet all criteria')

        if self.check_positive(num3) and self.check_even(num3) and self.check_magnitude(num3):
            status.append('Positive, Even, Less than 100')
        else:
            status.append('Does not meet all criteria')

        report['status'] = status
        return report

if __name__ == '__main__':
    validator = Validator()
    result = validator.combine_and_report(10, 50, 200)
    print(result)