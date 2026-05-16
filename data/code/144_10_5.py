def evaluate_boolean_expression(P, Q, expression):
    if expression == "P and Q":
        return P and Q
    elif expression == "P or Q":
        return P or Q
    elif expression == "not P":
        return not P
    elif expression == "not Q":
        return not Q
    elif expression == "P and not Q":
        return P and (not Q)
    elif expression == "P or not Q":
        return P or (not Q)
    elif expression == "P and Q or Q":
        return (P and Q) or Q
    elif expression == "P and not Q or Q":
        return (P and (not Q)) or Q
    elif expression == "P or Q and not P":
        return (P or Q) and (not P)
    elif expression == "not P or Q and not P":
        return (not P) or (Q and (not P))
    else:
        raise ValueError("Unsupported expression")
if __name__ == '__main__':
    P_values = [False, True]
    Q_values = [False, True]
    expression = "P and Q"
    print("P | Q | Result")
    print("----|----|-------")
    for P in P_values:
        for Q in Q_values:
            result = evaluate_boolean_expression(P, Q, expression)
            print(f"{P} | {Q} | {result}")