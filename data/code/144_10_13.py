class TruthTableSolver:
    def __init__(self):
        self.lookup = {
            'P and Q': lambda P, Q: P and Q,
            'P or Q': lambda P, Q: P or Q,
            'not P': lambda P, Q: not P,
            'not Q': lambda P, Q: not Q,
            'P and not Q': lambda P, Q: P and (not Q),
            'P or not Q': lambda P, Q: P or (not Q),
            'P and Q or Q': lambda P, Q: (P and Q) or Q,
            'P or Q and Q': lambda P, Q: P or (Q and Q)
        }

    def evaluate(self, expression, P, Q):
        return self.lookup[expression](P, Q)

if __name__ == '__main__':
    solver = TruthTableSolver()
    print(solver.evaluate('P and Q', True, False))
    print(solver.evaluate('P or Q', False, False))
    print(solver.evaluate('not P', True, True))
    print(solver.evaluate('P and not Q', True, False))