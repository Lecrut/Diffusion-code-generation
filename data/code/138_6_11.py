def truth_table():
    for A in [False, True]:
        for B in [False, True]:
            implication = not A or B
            equivalence = A == B
            print(f"A: {A}, B: {B}, Implication (A -> B): {implication}, Equivalence (A == B): {equivalence}")

if __name__ == '__main__':
    truth_table()