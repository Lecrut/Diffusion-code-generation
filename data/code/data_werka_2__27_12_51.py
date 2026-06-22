class InequalityChecker:
    @staticmethod
    def check_inequality(a, b):
        if type(a) is not type(b):
            return True
        return a != b

if __name__ == '__main__':
    test_values = [
        (5, 10),
        (5.0, 10.0),
        ('hello', 'world'),
        ([1, 2], [3, 4]),
        ({'a': 1}, {'b': 2}),
        (True, False),
        (None, None),
        (1 + 2j, 3 + 4j)
    ]
    for a, b in test_values:
        result = InequalityChecker.check_inequality(a, b)
        print(result)