import itertools

def generate_truth_table():
    variables = ['A', 'B', 'C']
    truth_values = list(itertools.product([True, False], repeat=3))
    
    for values in truth_values:
        A, B, C = values
        print(f"{A} {B} {C}")

if __name__ == '__main__':
    generate_truth_table()