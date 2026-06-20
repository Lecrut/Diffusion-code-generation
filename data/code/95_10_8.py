class Validator:
    def combine_and_report(self, a, b, c):
        report = {
            'a': a,
            'b': b,
            'c': c,
            'status': []
        }
        
        if a > 0 and a % 2 == 0 and a < 100:
            report['status'].append('a is positive, even, and less than 100')
        else:
            report['status'].append('a does not meet the criteria')
        
        if b > 0 and b % 2 == 0 and b < 100:
            report['status'].append('b is positive, even, and less than 100')
        else:
            report['status'].append('b does not meet the criteria')
        
        if c > 0 and c % 2 == 0 and c < 100:
            report['status'].append('c is positive, even, and less than 100')
        else:
            report['status'].append('c does not meet the criteria')
        
        return report

if __name__ == '__main__':
    validator = Validator()
    result = validator.combine_and_report(2, 4, 6)
    print(result)