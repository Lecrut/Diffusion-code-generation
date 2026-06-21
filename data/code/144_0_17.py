def compute_expression(A, B, C):
    return (A and B) or not C

if __name__ == '__main__':
    sample_values = {
        'A': True,
        'B': False,
        'C': True
    }
    
    print(f"A: {sample_values['A']}, B: {sample_values['B']}, C: {sample_values['C']} -> {(compute_expression(sample_values['A'], sample_values['B'], sample_values['C']))}")