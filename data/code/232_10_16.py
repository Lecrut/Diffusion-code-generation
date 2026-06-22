def fibonacci_like_sequence(limit):
    if limit <= 0:
        return []
    elif limit == 1:
        return [1]
    elif limit == 2:
        return [1, 2]

    sequence = [1, 2]
    for _ in range(2, limit):
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence

if __name__ == '__main__':
    result = fibonacci_like_sequence(10)
    print(*result)