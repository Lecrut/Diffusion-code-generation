def truth_table():
    A = True
    B = False
    C = True
    
    print(f"A: {A}, B: {B}, C: {C}")
    print(f"(A AND B) OR (NOT C): {(A and B) or not C}")

if __name__ == '__main__':
    truth_table()