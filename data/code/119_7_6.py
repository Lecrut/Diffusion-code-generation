def reverse_order(a: float, b: float) -> (float, float):
    if not isinstance(a, float) or not isinstance(b, float):
        raise ValueError("Both inputs must be floats.")
    return b, a

if __name__ == '__main__':
    print(reverse_order(3.14, 2.71))