def implication(a, b):
    return not a or b

if __name__ == '__main__':
    for A in [False, True]:
        for B in [False, True]:
            print(f"A: {A}, B: {B}, A IMPLIES B: {implication(A, B)}")