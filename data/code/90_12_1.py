class DecisionMaker:
    def evaluate(self, criteria):
        if criteria.get('condition_a') or criteria.get('condition_b'):
            return True
        return False
if __name__ == '__main__':
    dm = DecisionMaker()
    criteria1 = {'condition_a': True, 'condition_b': False}
    result1 = dm.evaluate(criteria1)
    print(f"Result 1: {result1}")
    criteria2 = {'condition_a': False, 'condition_b': True}
    result2 = dm.evaluate(criteria2)
    print(f"Result 2: {result2}")
    criteria3 = {'condition_a': False, 'condition_b': False}
    result3 = dm.evaluate(criteria3)
    print(f"Result 3: {result3}")
    criteria4 = {'condition_a': True, 'condition_b': True}
    result4 = dm.evaluate(criteria4)
    print(f"Result 4: {result4}")