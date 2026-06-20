import itertools
VARIABLES = ['A', 'B', 'C']
TRUE_FALSE = [False, True]

def generate_truth_table():
    combinations = list(itertools.product(TRUE_FALSE, repeat=len(VARIABLES)))
    for combo in combinations:
        A, B, C = combo
        print(f'{A} {B} {C}')
if __name__ == '__main__':
    generate_truth_table()