class MultiAttributeVerifier:
    VERIFICATION_MAP = {
        'a_positive': lambda self: self.a > 0,
        'b_even': lambda self: self.b % 2 == 0,
        'c_div_a': lambda self: self.c % self.a == 0,
    }

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def verify_all(self):
        checks = list(self.VERIFICATION_MAP.values())
        results = []
        for check in checks:
            results.append(check(self))
        return all(results)

if __name__ == '__main__':
    verifier = MultiAttributeVerifier(3, 6, 12)
    outcome = verifier.verify_all()
    print(outcome)