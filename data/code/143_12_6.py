from pysat.solvers import Glucose3

def validate_pair(pair):
    if not isinstance(pair, (list, tuple)) or len(pair) != 2:
        raise ValueError("Input must be a pair of statements.")

def convert_to_cnf(statement):
    cnf = []
    parts = statement.split(' ')
    for part in parts:
        if part.startswith('not '):
            cnf.append(-int(part[4:]))
        else:
            cnf.append(int(part))
    return cnf

def is_contradictory(pair):
    validate_pair(pair)
    solver = Glucose3()
    for statement in pair:
        solver.add_clause(convert_to_cnf(statement))
    return not solver.solve()

if __name__ == '__main__':
    print(is_contradictory(['1', 'not 1']))
    print(is_contradictory(['2', '3']))