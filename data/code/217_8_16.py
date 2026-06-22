def are_decimals_equal(a, b, epsilon=1e-9):
    if math.isnan(a) or math.isnan(b):
        return a == b
    if math.isinf(a) or math.isinf(b):
        return a == b
    return abs(a - b) <= epsilon

if __name__ == '__main__':
    sample_a = 0.1 + 0.2
    sample_b = 0.3
    print(are_decimals_equal(sample_a, sample_b))
    
    sample_c = float('nan')
    sample_d = float('nan')
    print(are_decimals_equal(sample_c, sample_d))
    
    sample_e = float('inf')
    sample_f = float('inf')
    print(are_decimals_equal(sample_e, sample_f))
    
    sample_g = float('-inf')
    sample_h = float('-inf')
    print(are_decimals_equal(sample_g, sample_h))
    
    sample_i = float('inf')
    sample_j = float('nan')
    print(are_decimals_equal(sample_i, sample_j))