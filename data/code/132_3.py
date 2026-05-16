def determine_state(A, B, C):
    return (A and B) or (A and C) or (B and C)
if __name__ == '__main__':
    print(determine_state(True, True, False))
    print(determine_state(True, False, False))
    print(determine_state(False, True, False))
    print(determine_state(False, False, True))
    print(determine_state(True, True, True))
    print(determine_state(False, False, False))