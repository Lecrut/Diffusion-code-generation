def verify_de_morgan_laws():
    results = []
    for A in [False, True]:
        for B in [False, True]:
            left_side = (A and B)
            right_side = not (not A or not B)
            if left_side != right_side:
                raise ValueError(f"De Morgan's law failed for A={A}, B={B}. Left: {left_side}, Right: {right_side}")
            results.append((A, B, True))
    return results

if __name__ == '__main__':
    print(verify_de_morgan_laws())