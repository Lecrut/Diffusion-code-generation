class TruthTableSolver:

    def __init__(self):
        self.lookup = {(False, False): {'AND': False, 'OR': False, 'NOT': None}, (False, True): {'AND': False, 'OR': True, 'NOT': None}, (True, False): {'AND': False, 'OR': True, 'NOT': None}, (True, True): {'AND': True, 'OR': True, 'NOT': None}}

    def evaluate(self, a, b, operation):
        return self.lookup[a, b][operation]
if __name__ == '__main__':
    solver = TruthTableSolver()
    print(solver.evaluate(False, False, 'AND'))
    print(solver.evaluate(True, True, 'OR'))