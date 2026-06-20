def evaluate_logic(a: bool, b: bool, c: bool) -> bool:
    and_result = a and b
    not_c = not c
    return and_result or not_c

if __name__ == '__main__':
    input_a = True
    input_b = False
    input_c = True
    result = evaluate_logic(input_a, input_b, input_c)
    print(f"Input A: {input_a}")
    print(f"Input B: {input_b}")
    print(f"Input C: {input_c}")
    print(f"Result of (a AND b) OR (NOT c): {result}")

    input_a = False
    input_b = True
    input_c = False
    result = evaluate_logic(input_a, input_b, input_c)
    print(f"Input A: {input_a}")
    print(f"Input B: {input_b}")
    print(f"Input C: {input_c}")
    print(f"Result of (a AND b) OR (NOT c): {result}")