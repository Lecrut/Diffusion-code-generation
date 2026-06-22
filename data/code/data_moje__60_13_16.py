def compute_factorial():
    n = 10
    result = 1
    while True:
        if n <= 1:
            break
        result *= n
        n -= 1
    return result

if __name__ == '__main__':
    print(compute_factorial())