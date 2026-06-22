def build_fibonacci_sequence(count: int) -> list:
    if count <= 0:
        return []
    if count == 1:
        return [0]
    result = [0, 1]
    [result.append(result[-1] + result[-2]) for _ in range(count - 2)]
    return result

if __name__ == '__main__':
    target_n = 15
    sequence = build_fibonacci_sequence(target_n)
    print(sequence)