class Validator:
    def combine_and_report(self, num1, num2, num3):
        checks = {
            'num1': {'positive': num1 > 0, 'even': num1 % 2 == 0, 'less_than_100': num1 < 100},
            'num2': {'positive': num2 > 0, 'even': num2 % 2 == 0, 'less_than_100': num2 < 100},
            'num3': {'positive': num3 > 0, 'even': num3 % 2 == 0, 'less_than_100': num3 < 100}
        }
        reports = {key: all(value.values()) for key, value in checks.items()}
        return {'inputs': [num1, num2, num3], 'reports': reports}

if __name__ == '__main__':
    validator = Validator()
    result = validator.combine_and_report(10, 50, 200)
    print(result)