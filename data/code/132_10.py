def logical_and(a: bool, b: bool) -> bool:
    return a and b
if __name__ == '__main__':
    input_a = True
    input_b = False
    result = logical_and(input_a, input_b)
    print(f"Input A: {input_a}")
    print(f"Input B: {input_b}")
    print(f"Result of logical AND: {result}")
    input_a = True
    input_b = True
    result = logical_and(input_a, input_b)
    print(f"Input A: {input_a}")
    print(f"Input B: {input_b}")
    print(f"Result of logical AND: {result}")
    input_a = False
    input_b = True
    result = logical_and(input_a, input_b)
    print(f"Input A: {input_a}")
    print(f"Input B: {input_b}")
    print(f"Result of logical AND: {result}")