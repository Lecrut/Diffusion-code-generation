FIB_MEMO = {0: 0, 1: 1}

def fibonacci(n):
    if n not in FIB_MEMO:
        FIB_MEMO[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return FIB_MEMO[n]
if __name__ == '__main__':
    print(fibonacci(10))