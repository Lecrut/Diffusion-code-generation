from pysat.solvers import Glucose3

def is_contradictory(pair):
    solver = Glucose3()
    for statement in pair:
        solver.add(statement)
    return not solver.solve()

if __name__ == '__main__':
    contradictory_pair = [[1, -2], [-1, 2]]
    print(is_contradictory(contradictory_pair))