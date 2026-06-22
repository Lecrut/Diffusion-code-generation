def generate_fibonacci_sequence(count):
    if count <= 0:
        return []
    sequence = [0] * count
    if count == 1:
        sequence[0] = 0
        return sequence
    sequence[0] = 0
    sequence[1] = 1
    for index in range(2, count):
        prev_prev = sequence[index - 2]
        prev = sequence[index - 1]
        sequence[index] = prev_prev + prev
    return sequence

if __name__ == '__main__':
    result = generate_fibonacci_sequence(75)
    for number in result:
        print(number)