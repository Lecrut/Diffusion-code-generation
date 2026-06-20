def verify_de_morgan_laws():
    results = []
    for A in [False, True]:
        for B in [False, True]:
            left_side = (A and B)
            right_side = not (not A or not B)
            results.append((A, B, left_side == right_side))
    return results

if __name__ == '__main__':
    sample_a = False
    sample_b = True
    law_results = verify_de_morgan_laws()
    print(law_results)