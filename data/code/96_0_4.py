def evaluate_nested_logic(a: bool, b: bool, c: bool, d: bool) -> bool:
    return (a and b) or (c and not d)

if __name__ == '__main__':
    try:
        A = True
        B = False
        C = True
        D = False
        result = evaluate_nested_logic(A, B, C, D)
        print(result)
    except TypeError as e:
        print(f"Invalid input: {e}")