class DecisionMaker:
    def evaluate(self, criteria):
        if not isinstance(criteria, (list, tuple, set)):
            raise ValueError("Criteria must be an iterable of boolean values.")
        
        if len(criteria) == 0:
            return False
        
        return any(criteria)

if __name__ == '__main__':
    maker = DecisionMaker()
    result = maker.evaluate([False, False, True])
    print(result)