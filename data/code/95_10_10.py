class Validator:
    def combine_and_report(self, a, b, c):
        reports = {
            'a': self._check_number(a),
            'b': self._check_number(b),
            'c': self._check_number(c)
        }
        return reports

    def _check_number(self, number):
        is_positive = number > 0
        is_even = number % 2 == 0
        is_less_than_100 = number < 100
        if not is_positive:
            return {'status': 'not positive'}
        elif not is_even:
            return {'status': 'not even'}
        elif not is_less_than_100:
            return {'status': 'not less than 100'}
        else:
            return {'status': 'positive, even, and less than 100'}

if __name__ == '__main__':
    validator = Validator()
    result = validator.combine_and_report(10, 50, 200)
    print(result)