def generate_truth_table(variables):
    header = ' | '.join(variables + ['AND', 'OR', 'XOR'])
    print(header)
    print('-' * len(header))
    
    for combination in itertools.product([True, False], repeat=len(variables)):
        row_values = [str(val) for val in combination]
        and_val = all(combination)
        or_val = any(combination)
        xor_val = any(val != other for val, other in zip(combination, combination[1:]))
        
        print(' | '.join(row_values + [and_val, or_val, xor_val]))

if __name__ == '__main__':
    sample_variables = ['P', 'Q']
    generate_truth_table(sample_variables)