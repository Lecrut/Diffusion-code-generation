def evaluate_nested_logic(a, b, c, d):
    if not all(isinstance(arg, bool) for arg in (a, b, c, d)):
        raise ValueError("Arguments must be boolean")
    
    ab_result = a and b
    cd_result = c and (not d)
    
    return ab_result or cd_result

if __name__ == '__main__':
    val_a = True
    val_b = False
    val_c = True
    val_d = False
    
    computed_result = evaluate_nested_logic(val_a, val_b, val_c, val_d)
    print(computed_result)