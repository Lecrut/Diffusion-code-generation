class DecisionMaker:
    def evaluate(self, criteria):
        return criteria.get('condition_a', False) or criteria.get('condition_b', False)
if __name__ == '__main__':
    dm = DecisionMaker()
    criteria1 = {'condition_a': True, 'condition_b': False}
    result1 = dm.evaluate(criteria1)
    print(f"Criteria 1 result: {result1}")
    criteria2 = {'condition_a': False, 'condition_b': True}
    result2 = dm.evaluate(criteria2)
    print(f"Criteria 2 result: {result2}")
    criteria3 = {'condition_a': False, 'condition_b': False}
    result3 = dm.evaluate(criteria3)
    print(f"Criteria 3 result: {result3}")
    criteria4 = {'condition_a': True, 'condition_b': True}
    result4 = dm.evaluate(criteria4)
    print(f"Criteria 4 result: {result4}")