def and_gate(a, b):
    try:
        a_val = int(a)
        b_val = int(b)
        return a_val & b_val
    except ValueError:
        raise TypeError("Inputs must be valid integers or binary strings.")
if __name__ == '__main__':
    print(and_gate("101", "110"))
    print(and_gate(1, 0))
    print(and_gate("1", "0"))
    try:
        print(and_gate("101", "invalid"))
    except TypeError as e:
        print(f"Error caught: {e}")
    try:
        print(and_gate(5, "2"))
    except TypeError as e:
        print(f"Error caught: {e}")