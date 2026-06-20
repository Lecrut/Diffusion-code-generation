class DecisionMaker:
    def evaluate(self, criteria):
        return any(criteria)

if __name__ == '__main__':
    dm = DecisionMaker()
    print(dm.evaluate([False, False, True]))