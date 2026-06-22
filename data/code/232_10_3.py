def fibonacci_like_sequence(limit):
    sequence = [1, 2]
    while len(sequence) < limit:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence[:limit]

if __name__ == '__main__':
    result = fibonacci_like_sequence(10)
    print(*result)