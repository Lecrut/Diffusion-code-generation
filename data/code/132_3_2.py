def determine_state(A, B, C):
    return (A and B) or (A and C) or (B and C)
if __name__ == '__main__':
    print(f"A=True, B=True, C=True: {determine_state(True, True, True)}")
    print(f"A=True, B=True, C=False: {determine_state(True, True, False)}")
    print(f"A=True, B=False, C=False: {determine_state(True, False, False)}")
    print(f"A=False, B=False, C=False: {determine_state(False, False, False)}")
    print(f"A=True, B=False, C=True: {determine_state(True, False, True)}")
    print(f"A=False, B=True, C=True: {determine_state(False, True, True)}")
    print(f"A=True, B=True, C=False: {determine_state(True, True, False)}")