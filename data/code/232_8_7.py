def generate_sequence(start, end):
    sequence = [0] * (end - start + 1)
    for i in range(start, end + 1):
        sequence[i - start] = i
    return sequence

if __name__ == '__main__':
    print(generate_sequence(1, 5))