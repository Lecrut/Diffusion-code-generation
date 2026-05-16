class Validator:
    def combine_and_report(self, a, b, c):
        results = {}
        def check(n, name):
            if n <= 0:
                return False
            if n % 2 != 0:
                return False
            if n >= 100:
                return False
            return True
        status = {}
        if check(a, 'a'):
            status['a'] = 'Pass'
        else:
            status['a'] = 'Fail'
        if check(b, 'b'):
            status['b'] = 'Pass'
        else:
            status['b'] = 'Fail'
        if check(c, 'c'):
            status['c'] = 'Pass'
        else:
            status['c'] = 'Fail'
        results['inputs'] = {'a': a, 'b': b, 'c': c}
        results['status'] = status
        return results
if __name__ == '__main__':
    validator = Validator()
    sample_a = 10
    sample_b = 20
    sample_c = 99
    report = validator.combine_and_report(sample_a, sample_b, sample_c)
    print(report)