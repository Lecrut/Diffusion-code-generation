def calculate_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    prev = 0
    curr = 1
    
    for _ in range(2, n):
        next_val = prev + curr
        sequence.append(next_val)
        prev = curr
        curr = next_val
    
    return sequence

if __name__ == '__main__':
    limit = 100
    result = calculate_fibonacci(limit)
    for i in range(limit):
        print(f"F({i}) = {result[i]}")