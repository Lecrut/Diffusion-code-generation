def verify_de_morgan_laws():
    for A in [False, True]:
        for B in [False, True]:
            lhs = (A and B)
            rhs = not (not A or not B)
            assert lhs == rhs, f"De Morgan's law failed for A={A}, B={B}: {lhs} != {rhs}"

if __name__ == '__main__':
    verify_de_morgan_laws()