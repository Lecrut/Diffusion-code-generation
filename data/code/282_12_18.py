def calculate_total(sequence):
    return sum(element for element in sequence)

if __name__ == '__main__':
    sample_sequence_1 = [1, 2, 3, 4, 5]
    result_1 = calculate_total(sample_sequence_1)
    print(f"The total for {sample_sequence_1} is: {result_1}")
    
    sample_sequence_2 = [10.5, 20.75, 30.25, 40.5]
    result_2 = calculate_total(sample_sequence_2)
    print(f"The total for {sample_sequence_2} is: {result_2}")
    
    sample_sequence_3 = [-1.1, 5.5, -3.3, 10.0]
    result_3 = calculate_total(sample_sequence_3)
    print(f"The total for {sample_sequence_3} is: {result_3}")