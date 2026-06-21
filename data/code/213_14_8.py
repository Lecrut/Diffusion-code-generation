def fibonacci(n):
    result = [0, 1]
    for i in range(2, n):
        next_val = result[-1] + result[-2]
        if next_val > n:
            break
        result.append(next_val)
    return result[:n]

if __name__ == '__main__':
    sample_n = 15
    output = fibonacci(sample_n)
    print(output)