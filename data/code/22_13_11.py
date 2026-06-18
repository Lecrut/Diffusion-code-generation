def is_odd(n): return n % 2 == 1

if __name__ == '__main__':
    test_values = [4, 5, -3, 0]
    results = []
    for val in test_values:
        num = val
        # Concise single-line expression checking oddness
        result_expr = (num % 2 != 0) 
        is_odd(num)