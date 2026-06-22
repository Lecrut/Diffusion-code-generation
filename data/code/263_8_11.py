MEMO = {}

def fibonacci(n):
    if n in MEMO:
        return MEMO[n]
    if n <= 1:
        return n
    MEMO[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return MEMO[n]

if __name__ == '__main__':
    result = fibonacci(10)
    print(result)