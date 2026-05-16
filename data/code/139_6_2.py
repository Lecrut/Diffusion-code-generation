def and_gate(a, b):
    try:
        if isinstance(a, str) and all(c in '01' for c in a):
            a_val = int(a, 2)
        elif isinstance(a, int):
            a_val = a
        else:
            raise TypeError("Invalid type for input a")
        if isinstance(b, str) and all(c in '01' for c in b):
            b_val = int(b, 2)
        elif isinstance(b, int):
            b_val = b
        else:
            raise TypeError("Invalid type for input b")
        if not (isinstance(a_val, int) and isinstance(b_val, int)):
            raise TypeError("Internal error: converted values are not integers")
        return a_val & b_val
    except (ValueError, TypeError) as e:
        raise ValueError(f"Error processing inputs: {e}")
if __name__ == '__main__':
    print(and_gate("101", "110"))
    print(and_gate(1, 0))
    print(and_gate("10", 1))
    print(and_gate("111", "00"))
    try:
        print(and_gate("101", "123"))
    except ValueError as e:
        print(e)
    try:
        print(and_gate(5, "10"))
    except ValueError as e:
        print(e)