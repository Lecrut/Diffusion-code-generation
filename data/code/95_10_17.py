class Validator:
    def combine_and_report(self, a, b, c):
        report = {
            'a': a,
            'b': b,
            'c': c,
            'status': []
        }
        
        if a > 0:
            report['status'].append('a is positive')
        else:
            report['status'].append('a is not positive')
        
        if b % 2 == 0:
            report['status'].append('b is even')
        else:
            report['status'].append('b is not even')
        
        if c < 100:
            report['status'].append('c is less than 100')
        else:
            report['status'].append('c is not less than 100')
        
        return report

if __name__ == '__main__':
    validator = Validator()
    result = validator.combine_and_report(5, 6, 78)
    print(result)