def create_arithmetic_sequence(start=5, difference=3, count=15):
    sequence = []
    current_term = start
    for _ in range(count):
        sequence.append(current_term)
        current_term += difference
    return sequence

if __name__ == '__main__':
    sample_sequence = create_arithmetic_sequence(20, 7, 10)
    print(sample_sequence)