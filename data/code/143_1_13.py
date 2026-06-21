class ContradictionChecker:
    def __init__(self, expressions):
        self.expressions = expressions

    def has_contradiction(self):
        expr_set = set(self.expressions)
        return len(expr_set) < len(self.expressions)

if __name__ == '__main__':
    checker1 = ContradictionChecker([True, False, True])
    print(f"Expressions: [True, False, True], Contradiction: {checker1.has_contradiction()}")

    checker2 = ContradictionChecker([True, False])
    print(f"Expressions: [True, False], Contradiction: {checker2.has_contradiction()}")

    checker3 = ContradictionChecker([True, True, True])
    print(f"Expressions: [True, True, True], Contradiction: {checker3.has_contradiction()}")