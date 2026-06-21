class Validator:
    def combine_and_report(self, a, b, c):
        checks = {
            'a': self._validate(a),
            'b': self._validate(b),
            'c': self._validate(c)
        }
        statuses = []
        for k, v in checks.items():
            statuses.append(v)
        
        total = a + b + c
        return {
            'inputs': {'a': a, 'b': b, 'c': c},
            'statuses': statuses,
            'sum': total,
            'all_valid': all('valid' in s for s in statuses)
        }

    def _validate(self, val):
        if val <= 0:
            return "not positive"
        if val % 2 != 0:
            return "odd"
        if val >= 100:
            return "too large"
        return "valid"

if __name__ == '__main__':
    v = Validator()
    
    report1 = v.combine_and_report(10, 20, 30)
    print(report1['sum'])
    print(report1['all_valid'])
    
    report2 = v.combine_and_report(-5, 99, 0)
    print(report2['sum'])
    print(report2['all_valid'])