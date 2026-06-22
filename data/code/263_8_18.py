FIB_MEMO = {}

def fibonacci(n):
    if n in FIB_MEMO:
        return FIB_MEMO[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    FIB_MEMO[n] = result
    return result
if __name__ == '__main__':
    print(fibonacci(10))
    print(fibonacci(1))
    print(fibonacci(8))