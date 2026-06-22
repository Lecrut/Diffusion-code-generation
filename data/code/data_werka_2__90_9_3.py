class DecisionMaker:
    def evaluate(self, criteria):
        if not isinstance(criteria, (list, tuple)):
            raise ValueError("Criteria must be a list or tuple")
        
        if len(criteria) == 0:
            return False
        
        return any(criteria)

if __name__ == '__main__':
    dm = DecisionMaker()
    result = dm.evaluate([False, False, True])
    print(result)