def evaluate(A: bool, B: bool, C: bool, D: bool) -> bool:
    if not isinstance(A, bool):
        raise ValueError("A must be a boolean")
    if not isinstance(B, bool):
        raise ValueError("B must be a boolean")
    if not isinstance(C, bool):
        raise ValueError("C must be a boolean")
    if not isinstance(D, bool):
        raise ValueError("D must be a boolean")
    return bool((A and B) or (C and not D))

if __name__ == '__main__':
    val_A = True
    val_B = False
    val_C = True
    val_D = False
    output = evaluate(val_A, val_B, val_C, val_D)
    print(output)