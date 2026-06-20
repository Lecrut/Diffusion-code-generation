import itertools

def generate_truth_table():
    variables = ['A', 'B', 'C']
    combinations = list(itertools.product([False, True], repeat=3))
    
    for combination in combinations:
        A, B, C = combination
        print(f"{A} {B} {C}")

if __name__ == '__main__':
    generate_truth_table()