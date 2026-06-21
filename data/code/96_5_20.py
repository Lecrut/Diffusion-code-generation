import functools
import operator

VAR_A = 'A'
VAR_B = 'B'
VAR_C = 'C'
VAR_D = 'D'

def evaluate_expression(inputs):
    results = []
    for input_tuple in inputs:
        var_dict = dict(input_tuple)
        val_a = var_dict.get(VAR_A, False)
        val_b = var_dict.get(VAR_B, False)
        val_c = var_dict.get(VAR_C, False)
        val_d = var_dict.get(VAR_D, False)
        
        left_side = val_a and val_b
        right_side = val_c and not val_d
        
        result = left_side or right_side
        results.append(result)
    return results

if __name__ == '__main__':
    sample_data = [
        [('A', True), ('B', True), ('C', False), ('D', False)],
        [('A', False), ('B', False), ('C', True), ('D', True)],
        [('A', True), ('B', False), ('C', True), ('D', False)],
        [('A', False), ('B', True), ('C', False), ('D', True)],
    ]
    print(evaluate_expression(sample_data))