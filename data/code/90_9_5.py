class DecisionMaker:
    def __init__(self, criteria):
        self.criteria = criteria

    def evaluate(self):
        return any(self.criteria.values())

if __name__ == '__main__':
    dm = DecisionMaker({'is_admin': False, 'has_key': True, 'is_guest': False})
    result = dm.evaluate()
    print(result)