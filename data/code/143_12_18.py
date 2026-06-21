from pysat.solvers import Glucose3

def convert_to_cnf(statement):
    return statement.replace('and', ' & ').replace('or', ' | ')

def is_contradictory(pair):
    cnf1 = convert_to_cnf(pair[0])
    cnf2 = convert_to_cnf(pair[1])
    solver = Glucose3()
    solver.add_clause(cnf1.split())
    solver.add_clause([~int(x) for x in cnf2.split()])
    return not solver.solve()
if __name__ == '__main__':
    sample_pair = ('A and B', 'not A or not B')
    print(is_contradictory(sample_pair))