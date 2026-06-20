def verify_de_morgan_laws():
    de_morgan_results = []
    for A in [False, True]:
        for B in [False, True]:
            left_side = (A and B)
            right_side = not (not A or not B)
            de_morgan_results.append((A, B, left_side == right_side))
    return de_morgan_results

if __name__ == '__main__':
    de_morgan_table = verify_de_morgan_laws()
    print(de_morgan_table)