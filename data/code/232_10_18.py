MAX_SEQUENCE_LENGTH = 10

def fibonacci_like_sequence(limit):
    if limit <= 0:
        return []
    
    sequence = [1, 2]
    while len(sequence) < limit:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    
    return sequence[:limit]

if __name__ == '__main__':
    result = fibonacci_like_sequence(MAX_SEQUENCE_LENGTH)
    print(*result)