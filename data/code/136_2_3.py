import itertools
if __name__ == '__main__':
    a = True
    b = False
    operations = [
        ('and', lambda x, y: x and y),
        ('or', lambda x, y: x or y),
        ('xor', lambda x, y: x ^ y),
        ('not', lambda x: not x)
    ]
    results = []
    for op_type, func in operations:
        if op_type == 'not':
            results.append(func(a))
        else:
            results.append(func(a, b))
    print(f"a = {a}, b = {b}")
    print("AND results:")
    print(f"a AND b: {a and b}")
    print("OR results:")
    print(f"a OR b: {a or b}")
    print("XOR results:")
    print(f"a XOR b: {a ^ b}")
    print("NOT results:")
    print(f"NOT a: {not a}")
    print(f"NOT b: {not b}")