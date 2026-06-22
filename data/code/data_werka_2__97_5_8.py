def build_truth_table(num_inputs, logical_expr):
    if not isinstance(num_inputs, int) or num_inputs < 1:
        raise ValueError("num_inputs must be a positive integer")
    if not callable(logical_expr):
        raise ValueError("logical_expr must be a callable")
    
    inputs = [chr(ord('A') + i) for i in range(num_inputs)]
    total_combinations = 2 ** num_inputs
    
    header_parts = inputs + ['Result']
    print(' | '.join(f'{h:<10}' for h in header_parts))
    print('-' * (11 * num_inputs + 2 * (num_inputs - 1) + 10))
    
    results = []
    for i in range(total_combinations):
        current_values = []
        for j in range(num_inputs):
            bit = (i >> (num_inputs - 1 - j)) & 1
            current_values.append(bool(bit))
        
        result_val = logical_expr(*current_values)
        row_vals = [str(v) for v in current_values] + [str(result_val)]
        print(' | '.join(f'{v:<10}' for v in row_vals))
        results.append((current_values, result_val))
        
    return results

def sample_logic(a, b, c, d):
    return (a and b) or (not c and d)

if __name__ == '__main__':
    outputs = build_truth_table(4, sample_logic)
    print(outputs[-1])