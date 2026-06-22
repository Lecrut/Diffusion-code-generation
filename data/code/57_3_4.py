def generate_fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    sequence: list[int] = [0, 1]
    index: int = 2
    while index < n:
        next_val: int = sequence[index - 1] + sequence[index - 2]
        sequence.append(next_val)
        index += 1
    return sequence

if __name__ == '__main__':
    result = generate_fibonacci(500)
    print(result[499])