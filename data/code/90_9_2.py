class DecisionMaker:
    def evaluate(self, criteria):
        if not isinstance(criteria, (list, tuple, set)):
            raise ValueError("Criteria must be an iterable of boolean values.")
        
        if not criteria:
            return False
        
        return any(criteria)

if __name__ == '__main__':
    dm = DecisionMaker()
    result = dm.evaluate([False, False, True])
    print(result)