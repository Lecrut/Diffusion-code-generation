def compute_factorial_do_while(n):
    result = 1
    while True:
        result *= n
        n -= 1
        if n <= 1:
            break
    return result

if __name__ == '__main__':
    sample_value = 10
    result = compute_factorial_do_while(sample_value)
    print(result)