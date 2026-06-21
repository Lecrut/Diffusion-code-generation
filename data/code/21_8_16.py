def find_largest(a: float, b: float, c: float) -> float:
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    return max_val

if __name__ == '__main__':
    result = find_largest(10, 25, 15)
    print(result)