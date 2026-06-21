import pycosat

def convert_to_cnf(statement):
    return statement

def find_contradictory_pairs(statements):
    cnf_statements = [convert_to_cnf(stmt) for stmt in statements]
    pairs = []
    for i in range(len(cnf_statements)):
        for j in range(i + 1, len(cnf_statements)):
            combined_cnf = cnf_statements[i] + cnf_statements[j]
            if pycosat.solve(combined_cnf) == 'UNSAT':
                pairs.append((i, j))
    return pairs
if __name__ == '__main__':
    sample_statements = ['(A and B) or (not A)', '(C and D) or (not C)', '(E and F) or (not E)']
    contradictory_pairs = find_contradictory_pairs(sample_statements)
    print(contradictory_pairs)