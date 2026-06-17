def arithmetic_operations(a, b, c):
    results = {}
    try:
        results['sum'] = a + b + c
        results['difference'] = a - b
        results['product'] = a * b * c
        if b != 0:
            results['division'] = a / b
        else:
            results['division'] = "Undefined (Division by zero)"
    except TypeError:
        return {"error": "Invalid input types"}
    return results
if __name__ == '__main__':
    a_val = 10
    b_val = 2
    c_val = 5
    output1 = arithmetic_operations(a_val, b_val, c_val)
    print(f"Input: a={a_val}, b={b_val}, c={c_val}")
    print(output1)
    a_val = 10
    b_val = 0
    c_val = 5
    output2 = arithmetic_operations(a_val, b_val, c_val)
    print(f"\nInput: a={a_val}, b={b_val}, c={c_val}")
    print(output2)
    a_val = 10
    b_val = 2.5
    c_val = 3
    output3 = arithmetic_operations(a_val, b_val, c_val)
    print(f"\nInput: a={a_val}, b={b_val}, c={c_val}")
    print(output3)