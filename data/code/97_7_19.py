def generate_truth_table(variables):
    headers = ['P' + chr(65 + i) for i in range(len(variables))]
    operations = {
        'AND': lambda p, q: p and q,
        'OR': lambda p, q: p or q,
        'XOR': lambda p, q: p != q
    }
    
    header_row = ' | '.join(headers + ['P AND Q', 'P OR Q', 'P XOR Q'])
    separator = '-' * len(header_row)
    
    print(separator)
    print(header_row)
    print(separator)
    
    for combination in product([True, False], repeat=len(variables)):
        row_values = [str(var) for var in combination]
        and_q = operations['AND'](*combination)
        or_q = operations['OR'](*combination)
        xor_q = operations['XOR'](*combination)
        
        print(' | '.join(row_values + [str(and_q), str(or_q), str(xor_q)]))
    print(separator)

if __name__ == '__main__':
    sample_variables = ['P', 'Q']
    generate_truth_table(sample_variables)