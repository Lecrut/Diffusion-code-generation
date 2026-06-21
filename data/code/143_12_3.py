from pysat.solvers import Glucose3

def is_contradictory(pair):
    if not isinstance(pair, (list, tuple)) or len(pair) != 2:
        raise ValueError("Input must be a pair of statements.")
    
    solver = Glucose3()
    for statement in pair:
        parts = statement.split(' ')
        clause = []
        for p in parts:
            if p.startswith('not '):
                clause.append(-int(p[4:]))
            else:
                clause.append(int(p))
        solver.add_clause(clause)
    
    return not solver.solve()

if __name__ == '__main__':
    print(is_contradictory(['1', 'not 1']))
    print(is_contradictory(['2', '3']))