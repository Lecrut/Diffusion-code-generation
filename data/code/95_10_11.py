class Validator:
    def combine_and_report(self, a, b, c):
        report = {
            'a': a,
            'b': b,
            'c': c,
            'status': 'valid'
        }
        
        if not all(isinstance(x, int) for x in [a, b, c]):
            report['status'] = 'invalid: non-integer input'
        elif not all(x > 0 for x in [a, b, c]):
            report['status'] = 'invalid: non-positive input'
        elif not all(x % 2 == 0 for x in [a, b, c]):
            report['status'] = 'invalid: odd number input'
        elif not all(x < 100 for x in [a, b, c]):
            report['status'] = 'invalid: magnitude too large'
        
        return report

if __name__ == '__main__':
    validator = Validator()
    result = validator.combine_and_report(2, 4, 6)
    print(result)