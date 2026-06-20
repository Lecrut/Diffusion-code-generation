class Validator:
    def combine_and_report(self, a, b, c):
        if all(isinstance(x, int) for x in [a, b, c]):
            if all(x > 0 for x in [a, b, c]):
                if all(x < 100 for x in [a, b, c]):
                    if all(x % 2 == 0 for x in [a, b, c]):
                        return {'a': a, 'b': b, 'c': c, 'status': 'All checks passed'}
        return {'a': a, 'b': b, 'c': c, 'status': 'One or more checks failed'}

if __name__ == '__main__':
    validator = Validator()
    result = validator.combine_and_report(2, 4, 6)
    print(result)