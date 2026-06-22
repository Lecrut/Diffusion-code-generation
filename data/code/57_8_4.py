def fibonacci_sequence(n):
    if n < 0:
        return []
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    
    fibs = [0, 1]
    for i in range(2, n + 1):
        next_val = fibs[i-1] + fibs[i-2]
        fibs.append(next_val)
    return fibs

if __name__ == '__main__':
    result = fibonacci_sequence(1000)
    print(len(result))
    print(result[0])
    print(result[1])
    print(result[1000])