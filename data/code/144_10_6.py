def evaluate_boolean_expression(P, Q, expression):
    if expression == "P AND Q":
        return P and Q
    elif expression == "P OR Q":
        return P or Q
    elif expression == "NOT P":
        return not P
    elif expression == "NOT Q":
        return not Q
    elif expression == "P AND NOT Q":
        return P and (not Q)
    elif expression == "P OR NOT Q":
        return P or (not Q)
    elif expression == "P XOR Q":
        return P ^ Q
    elif expression == "P":
        return P
    elif expression == "Q":
        return Q
    else:
        raise ValueError("Unknown expression")
if __name__ == '__main__':
    P_values = [False, True]
    Q_values = [False, True]
    expression_to_evaluate = "P AND Q"
    print("P | Q | Result")
    print("-" * 15)
    for P in P_values:
        for Q in Q_values:
            result = evaluate_boolean_expression(P, Q, expression_to_evaluate)
            print(f"{P} | {Q} | {result}")