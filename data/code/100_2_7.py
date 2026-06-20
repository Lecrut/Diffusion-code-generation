def and_gate(a, b):
    return a and b

if __name__ == '__main__':
    input_a = True
    input_b = False
    result = and_gate(input_a, input_b)
    print(f"Input A: {input_a}")
    print(f"Input B: {input_b}")
    print(f"And gate result: {result}")