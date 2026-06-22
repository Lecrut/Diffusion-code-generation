def calculate_total(sequence):
    return sum(x for x in sequence)

if __name__ == '__main__':
    sample_sequence_1 = [1, 2, 3, 4, 5]
    result_1 = calculate_total(sample_sequence_1)
    print(f"The total for {sample_sequence_1} is: {result_1}")

    sample_sequence_2 = [10.5, -2.5, 3.5, 4.5]
    result_2 = calculate_total(sample_sequence_2)
    print(f"The total for {sample_sequence_2} is: {result_2}")

    sample_sequence_3 = []
    result_3 = calculate_total(sample_sequence_3)
    print(f"The total for {sample_sequence_3} is: {result_3}")