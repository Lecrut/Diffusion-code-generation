class TripleChecker:

    def validate(self, a, b, c):
        if not all((isinstance(x, (int, float)) and x > 0 for x in [a, b, c])):
            raise ValueError('All inputs must be positive numbers.')
        if not all((x % 2 == 0 for x in [a, b])):
            raise ValueError('Both a and b must be even numbers.')
        return (a + b) % c == 0
if __name__ == '__main__':
    checker = TripleChecker()
    print(checker.validate(2, 4, 6))
    print(checker.validate(1, 2, 3))