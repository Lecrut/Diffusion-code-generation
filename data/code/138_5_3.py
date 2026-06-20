import itertools

def generate_truth_table():
    variables = ['A', 'B', 'C']
    truth_values = list(itertools.product([False, True], repeat=3))
    
    for A, B, C in truth_values:
        print(f"{A} {B} {C}")

if __name__ == '__main__':
    generate_truth_table()