def evaluate_conditions(a, b, c, d):
    if not all(isinstance(x, int) and 0 <= x < 2 for x in (a, b, c, d)):
        raise ValueError("All inputs must be binary integers (0 or 1)")
    
    condition1 = (a & b) | (c & d)
    condition2 = (a | b) & (c | d)
    condition3 = a ^ b ^ c ^ d
    
    return condition1 or condition2 or condition3

if __name__ == '__main__':
    try:
        a_val = 1
        b_val = 2
        c_val = 0
        d_val = 1
        result = evaluate_conditions(a_val, b_val, c_val, d_val)
        print(result)
    except ValueError as e:
        print(e)