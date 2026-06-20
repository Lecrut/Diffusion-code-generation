import itertools

def generate_truth_table():
    variables = ['A', 'B', 'C']
    truth_values = list(itertools.product([False, True], repeat=3))
    
    for combo in truth_values:
        A, B, C = combo
        print(f"{A} {B} {C}")

if __name__ == '__main__':
    generate_truth_table()