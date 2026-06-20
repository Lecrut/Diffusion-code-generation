import itertools

def generate_truth_table():
    variables = ['A', 'B', 'C']
    combinations = list(itertools.product([True, False], repeat=3))
    
    print(f"{'A':<5}{'B':<5}{'C':<5}{'NOT A':<10}{'AND':<10}{'OR':<10}{'XOR':<10}")
    
    for combo in combinations:
        A, B, C = combo
        not_A = not A
        and_result = A and B and C
        or_result = A or B or C
        xor_result = (A and not B) or (not A and B)
        
        print(f"{A:<5}{B:<5}{C:<5}{not_A:<10}{and_result:<10}{or_result:<10}{xor_result:<10}")

if __name__ == '__main__':
    generate_truth_table()