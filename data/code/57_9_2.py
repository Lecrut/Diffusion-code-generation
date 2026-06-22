def generate_fibonacci_sequence(count):
    if count <= 0:
        return []
    sequence = [0] * count
    if count > 1:
        sequence[1] = 1
    for i in range(2, count):
        sequence[i] = sequence[i - 1] + sequence[i - 2]
    return sequence

if __name__ == '__main__':
    result = generate_fibonacci_sequence(75)
    print(result)