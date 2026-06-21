from pysat.solvers import Glucose3

def convert_to_cnf(statement):
    return statement.replace('and', ' & ').replace('or', ' | ')

def is_contradictory(pair):
    if not isinstance(pair, (list, tuple)) or len(pair) != 2:
        raise ValueError("Input must be a pair of statements.")
    
    cnf1 = convert_to_cnf(pair[0])
    cnf2 = convert_to_cnf(pair[1])
    
    solver = Glucose3()
    for clause in [cnf1.split(), [-int(x) for x in cnf2.split()]]:
        try:
            solver.add_clause(clause)
        except Exception as e:
            raise ValueError(f"Invalid statement format: {e}")
    
    return not solver.solve()

if __name__ == '__main__':
    sample_pairs = [('A and B', 'not A'), ('C or D', 'not C'), ('E and F', 'F')]
    results = [is_contradictory(pair) for pair in sample_pairs]
    print(results)