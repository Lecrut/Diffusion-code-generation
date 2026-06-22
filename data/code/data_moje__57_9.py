def get_first_75_fibonacci():
    if 75 < 2:
        return [0] if 75 == 0 else []
    sequence = [0, 1]
    current = 0
    while len(sequence) < 75:
        next_val = sequence[current] + sequence[current + 1]
        sequence.append(next_val)
        current += 1
    return sequence

if __name__ == '__main__':
    result = get_first_75_fibonacci()
    print(result)