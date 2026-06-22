def create_arithmetic_progression(start=5, difference=3, count=15):
    sequence = []
    current_term = start
    for _ in range(count):
        sequence.append(current_term)
        current_term += difference
    return sequence

if __name__ == '__main__':
    sample_start = 10
    sample_difference = 4
    sample_count = 20
    progression = create_arithmetic_progression(sample_start, sample_difference, sample_count)
    print(progression)