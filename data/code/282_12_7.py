def calculate_total(sequence):
    if not all(isinstance(x, (int, float)) for x in sequence):
        raise ValueError("All elements in the sequence must be numbers.")
    
    total = sum(element for element in sequence)
    return total

if __name__ == '__main__':
    sample_sequence_1 = [1.5, 2.3, 3.7, 4.1]
    result_1 = calculate_total(sample_sequence_1)
    print(f"The total for {sample_sequence_1} is: {result_1}")
    
    sample_sequence_2 = [-10, 5, -3, 10]
    result_2 = calculate_total(sample_sequence_2)
    print(f"The total for {sample_sequence_2} is: {result_2}")
    
    sample_sequence_3 = [0.0, 0.0, 0.0]
    result_3 = calculate_total(sample_sequence_3)
    print(f"The total for {sample_sequence_3} is: {result_3}")