def compute_factorial():
    n = 10
    result = 1
    i = 1
    while True:
        result *= i
        i += 1
        if i > n:
            break
    return result

if __name__ == '__main__':
    value = compute_factorial()
    print(value)