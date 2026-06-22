def calculate_total(sequence):
    total = 0.0
    for number in sequence:
        total += number
    return total

if __name__ == '__main__':
    sample_sequence = [1.23456, 7.89123, 4.32109, 0.98765]
    result = calculate_total(sample_sequence)
    print(result)