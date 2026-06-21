class TruthTableSolver:
    def __init__(self):
        self.lookup_table = {
            ('P', 'Q', 'and'): lambda P, Q: P and Q,
            ('P', 'Q', 'or'): lambda P, Q: P or Q,
            ('P', 'not'): lambda P: not P,
            ('Q', 'not'): lambda Q: not Q,
            ('P', 'Q', 'and', 'not'): lambda P, Q: P and (not Q),
            ('P', 'Q', 'or', 'not'): lambda P, Q: P or (not Q),
            ('P', 'Q', 'and', 'Q'): lambda P, Q: (P and Q) or Q,
            ('P', 'Q', 'and', 'not', 'P'): lambda P, Q: False,
            ('P', 'Q', 'or', 'Q'): lambda P, Q: P or (Q and Q)
        }

    def evaluate(self, P, Q, expression):
        return self.lookup_table[expression](P, Q)

if __name__ == '__main__':
    solver = TruthTableSolver()
    print(solver.evaluate(True, False, ('P', 'Q', 'and')))
    print(solver.evaluate(True, True, ('P', 'Q', 'or')))
    print(solver.evaluate(False, True, ('P', 'not')))
    print(solver.evaluate(True, False, ('Q', 'not')))
    print(solver.evaluate(True, False, ('P', 'Q', 'and', 'not')))
    print(solver.evaluate(True, True, ('P', 'Q', 'or', 'not')))
    print(solver.evaluate(False, False, ('P', 'Q', 'and', 'Q')))
    print(solver.evaluate(True, False, ('P', 'Q', 'and', 'not', 'P')))
    print(solver.evaluate(True, True, ('P', 'Q', 'or', 'Q')))