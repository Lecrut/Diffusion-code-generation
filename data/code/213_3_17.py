FIB_MEMO = {}

def fibonacci(n):
    if n in FIB_MEMO:
        return FIB_MEMO[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    FIB_MEMO[n] = result
    return result

if __name__ == '__main__':
    sample_n = 10
    print(f"Fibonacci({sample_n}) = {fibonacci(sample_n)}")