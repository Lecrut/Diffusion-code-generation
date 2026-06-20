def verify_de_morgan_laws():
    results = []
    for A in [True, False]:
        for B in [True, False]:
            lhs = (A and B)
            rhs = not (not A or not B)
            results.append((A, B, lhs == rhs))
    return results

if __name__ == '__main__':
    print(verify_de_morgan_laws())