def generate_sequence(start, end):
    sequence = list(range(start, end + 1))
    return sequence

if __name__ == '__main__':
    result = generate_sequence(1, 5)
    print(result)