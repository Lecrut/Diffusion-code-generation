def fibonacci_like_sequence(limit):
    if limit <= 0:
        raise ValueError("Limit must be greater than 0")
    
    sequence = [1, 2]
    while len(sequence) < limit:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    
    return sequence[:limit]

if __name__ == '__main__':
    try:
        result = fibonacci_like_sequence(10)
        print(*result)
    except ValueError as e:
        print(e)