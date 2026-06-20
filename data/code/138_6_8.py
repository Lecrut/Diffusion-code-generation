def implication(a, b):
    return not a or b

def equivalence(a, b):
    return a == b

if __name__ == '__main__':
    for A in [False, True]:
        for B in [False, True]:
            print(f"A: {A}, B: {B}")
            print(f"A -> B: {implication(A, B)}")
            print(f"A == B: {equivalence(A, B)}")