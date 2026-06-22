def calculate_average(sequence):
    if not sequence:
        return 0.0
    total_sum = sum(sequence)
    count = len(sequence)
    if count == 0:
        return 0.0
    return total_sum / count

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    average_result = calculate_average(sample_sequence)
    print(average_result)