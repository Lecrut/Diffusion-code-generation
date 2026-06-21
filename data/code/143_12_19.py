import pycosat

def convert_to_cnf(statement):
    return [statement]

def find_contradictory_pairs(statements):
    cnf_statements = []
    for statement in statements:
        cnf_statements.extend(convert_to_cnf(statement))
    for i in range(len(cnf_statements)):
        for j in range(i + 1, len(cnf_statements)):
            combined_cnf = cnf_statements[:i] + cnf_statements[i + 1:j] + cnf_statements[j + 1:]
            if not pycosat.solve(combined_cnf):
                return (cnf_statements[i], cnf_statements[j])
    return None
if __name__ == '__main__':
    sample_statements = [3, -2, 4, -5]
    contradictory_pair = find_contradictory_pairs(sample_statements)
    print(contradictory_pair)