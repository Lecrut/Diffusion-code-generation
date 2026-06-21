import itertools

def compute_truth_table():
    variables = ['A', 'B', 'C']
    truth_values = list(itertools.product([True, False], repeat=3))
    
    results = []
    for A, B, C in truth_values:
        result = (A and B) or not C
        results.append((A, B, C, result))
    
    return results

if __name__ == '__main__':
    truth_table = compute_truth_table()
    print(truth_table)