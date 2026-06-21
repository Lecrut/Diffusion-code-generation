def find_maximum(a, b, c):
    if not all(isinstance(x, int) for x in [a, b, c]):
        raise ValueError("All inputs must be integers")
    return max(a, b, c)

if __name__ == '__main__':
    result = find_maximum(15, 23, 7)
    print(result)