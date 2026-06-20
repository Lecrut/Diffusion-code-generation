def truth_table():
    print("A | B | A -> B | A == B")
    for a in [False, True]:
        for b in [False, True]:
            implication = not a or b
            equivalence = a == b
            print(f"{a} | {b} | {implication} | {equivalence}")

if __name__ == '__main__':
    truth_table()