class TruthTableSolver:

    def __init__(self):
        self.lookup = {(True, True, 'AND'): True, (True, False, 'AND'): False, (False, True, 'AND'): False, (False, False, 'AND'): False, (True, True, 'OR'): True, (True, False, 'OR'): True, (False, True, 'OR'): True, (False, False, 'OR'): False, (True, False, 'NOT'): False, (False, True, 'NOT'): True}

    def evaluate(self, a, b, operation):
        key = (a, b, operation)
        if key in self.lookup:
            return self.lookup[key]
        else:
            raise ValueError('Invalid operation or inputs')
if __name__ == '__main__':
    solver = TruthTableSolver()
    print(solver.evaluate(True, False, 'AND'))
    print(solver.evaluate(True, True, 'OR'))
    print(solver.evaluate(False, True, 'NOT'))