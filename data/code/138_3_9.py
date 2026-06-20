def verify_de_morgan_laws():
    for A in [False, True]:
        for B in [False, True]:
            lhs = (A and B)
            rhs = not (not A or not B)
            print(f"A={A}, B={B}: LHS={(lhs)}, RHS={(rhs)}")

if __name__ == '__main__':
    verify_de_morgan_laws()