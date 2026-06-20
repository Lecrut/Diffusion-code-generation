def truth_table():
    for a in [False, True]:
        for b in [False, True]:
            implication = not a or b
            equivalence = a == b
            print(f"A: {a}, B: {b}, A -> B: {implication}, A == B: {equivalence}")

if __name__ == '__main__':
    truth_table()