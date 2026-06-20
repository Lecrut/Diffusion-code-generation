import itertools

def calculate_truth_table(operator):
    P_values = [0, 1]
    Q_values = [0, 1]
    results = [(p, q, operator(p, q)) for p in P_values for q in Q_values]
    return results

if __name__ == '__main__':
    and_table = calculate_truth_table(lambda p, q: p & q)
    or_table = calculate_truth_table(lambda p, q: p | q)
    not_table = calculate_truth_table(lambda p, q: ~p)
    xor_table = calculate_truth_table(lambda p, q: p ^ q)
    nor_table = calculate_truth_table(lambda p, q: ~(p | q))
    nand_table = calculate_truth_table(lambda p, q: ~(p & q))

    print("P | Q | P AND Q")
    for p, q, result in and_table:
        print(f"{p} | {q} | {result}")
    
    print("\nP | Q | P OR Q")
    for p, q, result in or_table:
        print(f"{p} | {q} | {result}")
    
    print("\nP | NOT P")
    for p, _, result in not_table:
        print(f"{p} | {result}")
    
    print("\nP | Q | P XOR Q")
    for p, q, result in xor_table:
        print(f"{p} | {q} | {result}")
    
    print("\nP | Q | P NOR Q")
    for p, q, result in nor_table:
        print(f"{p} | {q} | {result}")
    
    print("\nP | Q | P NAND Q")
    for p, q, result in nand_table:
        print(f"{p} | {q} | {result}")