import itertools

def evaluate_expression(A, B, C):
    return (A and B) or not C

def generate_truth_table():
    variables = ['A', 'B', 'C']
    header = " | ".join(variables) + " | Result"
    print(header)
    print("-" * len(header))
    
    for A, B, C in itertools.product([False, True], repeat=3):
        result = evaluate_expression(A, B, C)
        row_str = f"{A} | {B} | {C} | {result}"
        print(row_str)

if __name__ == '__main__':
    generate_truth_table()