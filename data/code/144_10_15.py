class TruthTableSolver:

    def __init__(self):
        self.lookup = {(True, True, 'AND'): True, (True, False, 'AND'): False, (False, True, 'AND'): False, (False, False, 'AND'): False, (True, True, 'OR'): True, (True, False, 'OR'): True, (False, True, 'OR'): True, (False, False, 'OR'): False, (True, 'NOT'): not True, (False, 'NOT'): not False}

    def evaluate(self, a, b, operation):
        if isinstance(b, str) and operation == 'NOT':
            return self.lookup[a, b, operation]
        else:
            return self.lookup[a, b, operation]
if __name__ == '__main__':
    solver = TruthTableSolver()
    print(solver.evaluate(True, False, 'AND'))
    print(solver.evaluate(True, True, 'OR'))
    print(solver.evaluate(False, 'NOT'))