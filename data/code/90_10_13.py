class DecisionMaker:

    def evaluate(self, criteria):
        if not all((isinstance(x, bool) for x in criteria)):
            raise ValueError('All criteria must be boolean values')
        return any(criteria)
if __name__ == '__main__':
    dm = DecisionMaker()
    sample_criteria1 = [True, False, True]
    print(dm.evaluate(sample_criteria1))
    sample_criteria2 = [False, False, False]
    print(dm.evaluate(sample_criteria2))