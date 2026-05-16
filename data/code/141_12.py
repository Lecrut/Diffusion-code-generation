def evaluate_logic(A: bool, B: bool, C: bool) -> bool:
    result = (A and B) or (not C)
    return result
if __name__ == '__main__':
    A_val = True
    B_val = False
    C_val = True
    result = evaluate_logic(A_val, B_val, C_val)
    print(result)