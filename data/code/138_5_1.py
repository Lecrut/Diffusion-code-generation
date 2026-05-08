import itertools
def xor(a, b):
    return a != b
if __name__ == '__main__':
    booleans = [False, True]
    print("XOR Truth Table")
    print("-----------------")
    for a in booleans:
        for b in booleans:
            result = xor(a, b)
            print(f"A: {a}, B: {b} -> XOR: {result}")