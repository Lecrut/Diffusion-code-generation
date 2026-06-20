def verify_de_morgan_laws():
    for A in [False, True]:
        for B in [False, True]:
            left_side = (A and B)
            right_side = not (not A or not B)
            if left_side != right_side:
                return False
    return True

if __name__ == '__main__':
    result = verify_de_morgan_laws()
    print(result)