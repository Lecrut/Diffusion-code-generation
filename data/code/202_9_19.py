def find_maximum(a, b, c):
    if not all(isinstance(x, int) for x in [a, b, c]):
        raise ValueError("All inputs must be integers")
    return max(a, b, c)

if __name__ == '__main__':
    max_val = find_maximum(10, 20, 30)
    print(max_val)