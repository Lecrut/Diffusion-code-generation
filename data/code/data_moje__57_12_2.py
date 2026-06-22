def generate_fibonacci(count):
    if count <= 0:
        return []
    if count == 1:
        return [0]
    sequence = [0, 1]
    for _ in range(2, count):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if __name__ == '__main__':
    result = generate_fibonacci(20)
    print(result)