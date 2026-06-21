from pysat.solvers import Glucose3

def convert_to_cnf(statement):
    return statement.replace('and', ' & ').replace('or', ' | ').replace('not', '~')

def is_contradictory(pair):
    cnf1 = convert_to_cnf(pair[0])
    cnf2 = convert_to_cnf(pair[1])
    solver = Glucose3()
    solver.add_clause(cnf1.split())
    solver.add_clause([~int(x) for x in cnf2.split()])
    return not solver.solve()
if __name__ == '__main__':
    sample_pairs = [('A and B', 'not A'), ('C or D', 'not C'), ('E and F', 'F')]
    results = [is_contradictory(pair) for pair in sample_pairs]
    print(results)