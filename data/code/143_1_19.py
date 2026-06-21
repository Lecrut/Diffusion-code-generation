class ContradictionDetector:
    def __init__(self, expressions):
        self.expressions = expressions

    def has_contradiction(self):
        expression_set = set(self.expressions)
        true_set = expression_set.intersection([True])
        false_set = expression_set.intersection([False])
        
        if len(true_set) > 0 and len(false_set) > 0:
            return True
        return False

if __name__ == '__main__':
    detector1 = ContradictionDetector([True, False, True])
    print(f"Expressions: [True, False, True], Contradiction: {detector1.has_contradiction()}")

    detector2 = ContradictionDetector([True, False])
    print(f"Expressions: [True, False], Contradiction: {detector2.has_contradiction()}")

    detector3 = ContradictionDetector([True, True, True])
    print(f"Expressions: [True, True, True], Contradiction: {detector3.has_contradiction()}")