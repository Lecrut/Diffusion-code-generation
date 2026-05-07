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
    print(f"Result for criteria1: {result1}")
    print(f"Result for criteria2: {result2}")
    print(f"Result for criteria3: {result3}")
    print(f"Result for criteria4: {result4}")