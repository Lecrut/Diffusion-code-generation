def verify_de_morgan_law():
    results = []
    for A in [False, True]:
        for B in [False, True]:
            left_side = (A and B)
            right_side = not (not A or not B)
            results.append((A, B, left_side, right_side, left_side == right_side))
    return results

if __name__ == '__main__':
    sample_results = verify_de_morgan_law()
    for result in sample_results:
        print(result)