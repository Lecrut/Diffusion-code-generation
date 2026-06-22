def compute_average(sequence):
    if not sequence:
        return 0.0
    total_sum = sum(sequence)
    count = len(sequence)
    if count == 0:
        return 0.0
    average = total_sum / count
    return round(average, 6)

if __name__ == '__main__':
    sample_sequence = [123.456789, 234.567890, 345.678901]
    result = compute_average(sample_sequence)
    print(result)