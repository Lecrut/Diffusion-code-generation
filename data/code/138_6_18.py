def generate_truth_table():
    truth_values = {True: 'T', False: 'F'}
    operators = {'->': lambda A, B: not A or B, '==': lambda A, B: A == B}
    
    for operator, func in operators.items():
        print(f"Truth table for {operator}:")
        header = f"A\tB\t{operator}\tResult"
        print(header)
        print("-" * len(header))
        
        for A in [True, False]:
            for B in [True, False]:
                result = truth_values[func(A, B)]
                print(f"{A}\t{B}\t{operator}\t{result}")

if __name__ == '__main__':
    generate_truth_table()