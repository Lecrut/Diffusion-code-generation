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
    elif expression == "P or Q and Q":
        return P or (Q and Q)
    else:
        raise ValueError("Unknown expression")
if __name__ == '__main__':
    P_values = [False, True]
    Q_values = [False, True]
    expression_to_evaluate = "P and Q"
    print(f"Truth Table for expression: {expression_to_evaluate}\n")
    print("P | Q | Result")
    print("---|---|-------")
    for P in P_values:
        for Q in Q_values:
            result = evaluate_boolean_expression(P, Q, expression_to_evaluate)
            print(f"{P} | {Q} | {result}")