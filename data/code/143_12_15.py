from pysat.solvers import Glucose3

def convert_to_cnf(statement):
    return statement.replace('and', ' & ').replace('or', ' | ').replace('not', '~')

def check_unsat(cnf_statement):
    solver = Glucose3()
    clauses = cnf_statement.split(' & ')
    for clause in clauses:
        literals = clause.split(' | ')
        if not any((l.startswith('~') != literal.startswith('~') for literal in literals)):
            return False
        solver.add_clause([int(l[1:]) if l.startswith('~') else -int(l) for l in literals])
    return solver.solve() == False

def find_contradictory_pairs(statements):
    cnf_statements = [convert_to_cnf(statement) for statement in statements]
    contradictory_pairs = []
    for i, stmt1 in enumerate(cnf_statements):
        for j, stmt2 in enumerate(cnf_statements):
            if i != j and check_unsat(stmt1 + ' & ' + stmt2):
                contradictory_pairs.append((statements[i], statements[j]))
    return contradictory_pairs
if __name__ == '__main__':
    sample_statements = ['A and B', 'not A or C', 'B or not C']
    print(find_contradictory_pairs(sample_statements))