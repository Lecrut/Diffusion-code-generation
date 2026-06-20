class ConditionEvaluator:
    def __init__(self):
        self.conditions = {
            'greater than 10': lambda x: x > 10,
            'less than 0': lambda x: x < 0,
            'equal to active': lambda x: x == 'active'
        }

    def evaluate(self, value, condition):
        return self.conditions.get(condition, lambda _: False)(value)

if __name__ == '__main__':
    evaluator = ConditionEvaluator()
    print(evaluator.evaluate(5, 'greater than 10'))
    print(evaluator.evaluate(-3, 'less than 0'))
    print(evaluator.evaluate('active', 'equal to active'))