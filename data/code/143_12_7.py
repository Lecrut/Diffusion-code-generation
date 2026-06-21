from pysat.solvers import Glucose3

def is_contradictory(pair):
    solver = Glucose3()
    for statement in pair:
        if 'not' not in statement:
            solver.add_clause([int(statement)])
        else:
            clause = [-int(s.replace('not ', '')) for s in statement.split()]
            solver.add_clause(clause)
    return not solver.solve()

if __name__ == '__main__':
    print(is_contradictory(['1', 'not 1']))
    print(is_contradictory(['2', '3']))