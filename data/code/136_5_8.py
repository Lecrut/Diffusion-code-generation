def evaluate_complex_expression():
    sample_values = {'A': True, 'B': False, 'C': True, 'D': False}
    result = sample_values['A'] and (not sample_values['B']) or (sample_values['C'] and sample_values['D'])
    return result
if __name__ == '__main__':
    final_result = evaluate_complex_expression()
    print(final_result)