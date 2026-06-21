from pysat.solvers import Glucose3

def convert_to_cnf(statement):
    return statement

def are_contradictory(pair):
    cnf1 = convert_to_cnf(pair[0])
    cnf2 = convert_to_cnf(pair[1])
    solver = Glucose3()
    solver.add_clause(cnf1)
    solver.add_clause([-x for x in cnf2])
    return not solver.solve()
if __name__ == '__main__':
    sample_pair = (['A', 'B'], ['~A', '~B'])
    print(are_contradictory(sample_pair))