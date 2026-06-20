def print_implication_truth_table():
    inputs = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
    
    header = "P | Q | P -> Q\n"
    separator = "-" * len(header)
    
    print(header)
    print(separator)
    
    for input_combination in inputs:
        p, q = input_combination
        implication_result = not p or q
        print(f"{p} | {q} | {implication_result}")

if __name__ == '__main__':
    print_implication_truth_table()