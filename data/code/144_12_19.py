import itertools

def evaluate_expression(row):
    A, B, C = row
    return (A and B) or not C

def generate_truth_table():
    variables = ['A', 'B', 'C']
    header = " | ".join(variables) + " | Result"
    print(header)
    print("-" * len(header))
    
    for combination in itertools.product([False, True], repeat=3):
        row_values = list(combination)
        result = evaluate_expression(row_values)
        row_str = " | ".join(str(val).upper() for val in row_values) + " | " + ("T" if result else "F")
        print(row_str)

if __name__ == '__main__':
    generate_truth_table()