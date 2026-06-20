class ConditionEvaluator:
    CONDITIONS = {
        'greater than 10': lambda x: x > 10,
        'less than 0': lambda x: x < 0,
        'equal to active': lambda x: x == 'active'
    }

    @staticmethod
    def evaluate(value, condition):
        return ConditionEvaluator.CONDITIONS.get(condition, lambda _: False)(value)

if __name__ == '__main__':
    print(ConditionEvaluator.evaluate(5, 'greater than 10'))
    print(ConditionEvaluator.evaluate(-3, 'less than 0'))
    print(ConditionEvaluator.evaluate('active', 'equal to active'))