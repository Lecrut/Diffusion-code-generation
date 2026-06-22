def find_middle_index(sequence):
    sequence_length = len(sequence)
    is_even_length = (sequence_length % 2 == 0)
    if is_even_length:
        return sequence_length // 2 - 1
    else:
        return sequence_length // 2

if __name__ == '__main__':
    sample_odd_sequence = [10, 20, 30, 40, 50]
    sample_even_sequence = [10, 20, 30, 40, 50, 60]
    
    middle_index_odd = find_middle_index(sample_odd_sequence)
    middle_index_even = find_middle_index(sample_even_sequence)
    
    print(f"Middle index of odd sequence: {middle_index_odd}")
    print(f"Middle index of even sequence: {middle_index_even}")