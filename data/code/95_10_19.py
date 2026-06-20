class Validator:
    def combine_and_report(self, a, b, c):
        status = {
            'a': {'positive': a > 0, 'even': a % 2 == 0, 'magnitude': a < 100},
            'b': {'positive': b > 0, 'even': b % 2 == 0, 'magnitude': b < 100},
            'c': {'positive': c > 0, 'even': c % 2 == 0, 'magnitude': c < 100}
        }
        return {'inputs': {'a': a, 'b': b, 'c': c}, 'status': status}

if __name__ == '__main__':
    validator = Validator()
    result = validator.combine_and_report(5, 10, 99)
    print(result)