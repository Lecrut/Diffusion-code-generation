def evaluate_nested_logic(a, b, c, d):
    bools = [a, b, c, d]
    for val in bools:
        if type(val) is not bool:
            raise ValueError("Arguments must be booleans")
    term1 = bool(a and b)
    term2 = bool(c and (not d))
    return bool(term1 or term2)

if __name__ == '__main__':
    val_a = True
    val_b = False
    val_c = True
    val_d = False
    output = evaluate_nested_logic(val_a, val_b, val_c, val_d)
    print(output)