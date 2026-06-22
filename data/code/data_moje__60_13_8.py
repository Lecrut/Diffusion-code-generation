def compute_factorial_with_lookup():
    lookup = {1: 1}
    result = 1
    i = 1
    n = 10
    while True:
        result *= i
        lookup[i] = result
        i += 1
        if i > n:
            break
    return lookup[n]

if __name__ == '__main__':
    print(compute_factorial_with_lookup())