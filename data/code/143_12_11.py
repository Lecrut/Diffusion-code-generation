from pysat.solvers import Glucose3

def parse_statement(statement):
    if not isinstance(statement, str) or 'not' in statement:
        raise ValueError("Statement must be a string and cannot contain 'not'")
    return int(statement)

def is_contradictory(pair):
    if not isinstance(pair, (list, tuple)) or len(pair) != 2:
        raise ValueError("Input must be a pair of statements.")
    
    solver = Glucose3()
    for statement in pair:
        parsed_statement = parse_statement(statement)
        solver.add_clause([parsed_statement])
    
    return not solver.solve()

if __name__ == '__main__':
    print(is_contradictory(['1', 'not 1']))
    print(is_contradictory(['2', '3']))