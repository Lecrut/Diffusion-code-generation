class AttributeCombiner:
    CHECKS = {
        'a_positive': lambda obj: obj.a > 0,
        'b_even': lambda obj: obj.b % 2 == 0,
        'c_div_a': lambda obj: obj.a != 0 and obj.c % obj.a == 0,
    }

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def combine_checks(self):
        results = [check(self) for check in self.CHECKS.values()]
        return all(results)

if __name__ == '__main__':
    combiner = AttributeCombiner(2, 4, 8)
    output = combiner.combine_checks()
    print(output)