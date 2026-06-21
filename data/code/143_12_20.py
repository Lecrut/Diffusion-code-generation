import pycosat

def convert_to_cnf(statement):
    return statement

def is_contradictory(pair):
    cnf1 = convert_to_cnf(pair[0])
    cnf2 = convert_to_cnf(pair[1])
    combined_cnf = cnf1 + ['~' + literal for literal in cnf2]
    return pycosat.solve(combined_cnf) == 'UNSAT'
if __name__ == '__main__':
    sample_pair = ('A & B', '~B')
    print(is_contradictory(sample_pair))