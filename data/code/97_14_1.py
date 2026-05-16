import itertools
def xor(a, b):
    return a ^ b
if __name__ == '__main__':
    inputs = [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1)
    ]
    print("Binary Input Combinations and XOR Output:")
    for a, b in inputs:
        result = xor(a, b)
        print(f"Input: ({a}, {b}), Output: {result}")