def fibonacci_like_sequence(limit):
    sequence = [1, 2]
    for _ in range(2, limit):
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence[:limit]

if __name__ == '__main__':
    limit = 10
    result = fibonacci_like_sequence(limit)
    print(*result)