def fibonacci_sequence(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fibs: list[int] = [0, 1]
    for _ in range(2, n):
        next_val = fibs[-1] + fibs[-2]
        fibs.append(next_val)
    
    return fibs

if __name__ == '__main__':
    result = fibonacci_sequence(500)
    print(result)