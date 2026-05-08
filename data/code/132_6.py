def evaluate_complex_logic(P, Q):
    return not P or Q
if __name__ == '__main__':
    P_val = True
    Q_val = False
    result = evaluate_complex_logic(P_val, Q_val)
    print(result)
    P_val = False
    Q_val = True
    result = evaluate_complex_logic(P_val, Q_val)
    print(result)
    P_val = True
    Q_val = True
    result = evaluate_complex_logic(P_val, Q_val)
    print(result)
    P_val = False
    Q_val = False
    result = evaluate_complex_logic(P_val, Q_val)
    print(result)