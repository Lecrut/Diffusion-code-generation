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
    elif expression == "P IMPLIES Q":
        return (not P) or Q
    elif expression == "P IFF Q":
        return (P == Q)
    else:
        raise ValueError("Unknown expression")
if __name__ == '__main__':
    P_values = [False, True]
    Q_values = [False, True]
    expression = "P AND Q"
    print("P | Q | Result")
    print("---|---|-------")
    for P in P_values:
        for Q in Q_values:
            result = evaluate_boolean_expression(P, Q, expression)
            print(f"{P} | {Q} | {result}")