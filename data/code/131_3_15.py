def factorial(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    else:
        result = n * factorial(n - 1, memo)
        memo[n] = result
        return result

if __name__ == '__main__':
    sample_input = 5
    result = factorial(sample_input)
    print(f"Factorial of {sample_input} is {result}")