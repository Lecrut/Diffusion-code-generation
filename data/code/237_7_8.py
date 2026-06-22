def generate_even_numbers(start_value, length):
    sequence = []
    for _ in range(length):
        if start_value % 2 != 0:
            start_value += 1
        sequence.append(start_value)
        start_value += 2
    return sequence

if __name__ == '__main__':
    start = 1
    length = 10
    result = generate_even_numbers(start, length)
    print(result)