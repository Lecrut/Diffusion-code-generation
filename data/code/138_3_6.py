def verify_de_morgan_law():
    for A in [False, True]:
        for B in [False, True]:
            left_side = (A and B)
            right_side = not (not A or not B)
            assert left_side == right_side, f"De Morgan's law failed for A={A}, B={B}"

if __name__ == '__main__':
    verify_de_morgan_law()