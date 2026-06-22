def average_of_sequence(sequence):
    if not sequence:
        return 0.0
    try:
        total_sum = sum(sequence)
        count = len(sequence)
        average = total_sum / count
        return round(average, 6)
    except TypeError:
        raise ValueError('All elements in the sequence must be numbers')

if __name__ == '__main__':
    sample_values1 = [10, 20, 30, 40, 50]
    result1 = average_of_sequence(sample_values1)
    print(result1)

    sample_values2 = [1.5, 2.5, 3.5, 4.5, 5.5]
    result2 = average_of_sequence(sample_values2)
    print(result2)

    sample_values3 = []
    result3 = average_of_sequence(sample_values3)
    print(result3)

    sample_values4 = [10, 'twenty', 30]
    try:
        result4 = average_of_sequence(sample_values4)
        print(result4)
    except ValueError as e:
        print(e)