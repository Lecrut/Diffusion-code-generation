import itertools

def generate_truth_table():
    variables = ['A', 'B', 'C']
    combinations = list(itertools.product([False, True], repeat=3))
    if len(combinations) != 8:
        raise ValueError('Incorrect number of truth table combinations')
    for combo in combinations:
        A, B, C = combo
        print(f'{A} {B} {C}')
if __name__ == '__main__':
    generate_truth_table()