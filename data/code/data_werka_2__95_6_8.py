class ConditionEvaluator:
    CHECKS = {
        'a_positive': lambda val: val > 0,
        'b_even': lambda val: val % 2 == 0,
        'c_div_a': lambda vals: vals['c'] % vals['a'] == 0,
    }

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def evaluate(self):
        base_values = {
            'a': self.a,
            'b': self.b,
            'c': self.c,
        }
        results = []
        results.append(self.CHECKS['a_positive'](self.a))
        results.append(self.CHECKS['b_even'](self.b))
        results.append(self.CHECKS['c_div_a'](base_values))
        return all(results)

if __name__ == '__main__':
    evaluator = ConditionEvaluator(2, 4, 8)
    outcome = evaluator.evaluate()
    print(outcome)