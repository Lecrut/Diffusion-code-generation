import itertools
HEADER = 'A | B | C'

def generate_truth_table():
    combinations = list(itertools.product([False, True], repeat=3))
    print(HEADER)
    print('-' * len(HEADER))
    for A, B, C in combinations:
        print(f'{A} | {B} | {C}')
if __name__ == '__main__':
    generate_truth_table()