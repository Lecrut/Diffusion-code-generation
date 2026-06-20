def verify_de_morgan_law():
    results = []
    for A in [False, True]:
        for B in [False, True]:
            lhs = (A and B)
            rhs = not (not A or not B)
            results.append((A, B, lhs == rhs))
    return results

if __name__ == '__main__':
    print(verify_de_morgan_law())