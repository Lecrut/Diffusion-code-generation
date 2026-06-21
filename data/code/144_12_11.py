import itertools

def compute_truth_table():
    variables = ['A', 'B', 'C']
    combinations = list(itertools.product([True, False], repeat=3))
    
    truth_table = []
    for combo in combinations:
        A, B, C = combo
        result = (A and B) or not C
        truth_table.append((combo + (result,)))
    
    return truth_table

if __name__ == '__main__':
    print(compute_truth_table())