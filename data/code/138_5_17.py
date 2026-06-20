import itertools

def generate_truth_table():
    variables = ['A', 'B', 'C']
    combinations = list(itertools.product([False, True], repeat=3))
    
    for combo in combinations:
        A, B, C = combo
        print(f"{A} {B} {C} | {not (A and B or C)}")

if __name__ == '__main__':
    generate_truth_table()