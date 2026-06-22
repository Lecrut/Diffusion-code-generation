class DecisionMaker:
    def __init__(self, threshold=0.5):
        self.threshold = threshold

    def evaluate(self, criteria):
        if not isinstance(criteria, (list, tuple)):
            raise ValueError("Criteria must be a list or tuple.")
        if not criteria:
            return False
        true_count = sum(1 for c in criteria if c)
        return true_count >= self.threshold

if __name__ == '__main__':
    dm = DecisionMaker(threshold=1)
    result = dm.evaluate([False, True, False])
    print(result)