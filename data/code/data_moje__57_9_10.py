def get_fibonacci_sequence(count: int) -> list:
    if count <= 0:
        return []
    if count == 1:
        return [0]
    sequence = [0] * count
    sequence[1] = 1
    for i in range(2, count):
        sequence[i] = sequence[i - 1] + sequence[i - 2]
    return sequence

if __name__ == '__main__':
    result = get_fibonacci_sequence(75)
    for value in result:
        print(value)