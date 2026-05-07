class DecisionMaker:
    def evaluate(self, criteria):
        if criteria.get('condition_a') or criteria.get('condition_b'):
            return True
        return False
if __name__ == '__main__':
    dm = DecisionMaker()
    criteria1 = {'condition_a': True, 'condition_b': False}
    criteria2 = {'condition_a': False, 'condition_b': True}
    criteria3 = {'condition_a': False, 'condition_b': False}
    criteria4 = {'condition_a': True, 'condition_b': True}
    result1 = dm.evaluate(criteria1)
    result2 = dm.evaluate(criteria2)
    result3 = dm.evaluate(criteria3)
    result4 = dm.evaluate(criteria4)
    print(f"Criteria 1 evaluation: {result1}")
    print(f"Criteria 2 evaluation: {result2}")
    print(f"Criteria 3 evaluation: {result3}")
    print(f"Criteria 4 evaluation: {result4}")