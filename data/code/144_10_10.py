class TruthTableSolver:

    def __init__(self):
        self.lookup = {(False, False): {'AND': False, 'OR': False, 'NOT_A': True, 'NOT_B': True}, (False, True): {'AND': False, 'OR': True, 'NOT_A': True, 'NOT_B': False}, (True, False): {'AND': False, 'OR': True, 'NOT_A': False, 'NOT_B': True}, (True, True): {'AND': True, 'OR': True, 'NOT_A': False, 'NOT_B': False}}

    def evaluate(self, a, b, operation):
        return self.lookup[a, b][operation]
if __name__ == '__main__':
    solver = TruthTableSolver()
    print(solver.evaluate(False, False, 'AND'))
    print(solver.evaluate(True, True, 'OR'))