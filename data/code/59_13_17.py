def get_central_item(sequence):
    def validate_sequence(seq):
        if not isinstance(seq, (list, tuple)):
            raise ValueError("Input must be a list or a tuple")
        return seq

    validated_seq = validate_sequence(sequence)
    length = len(validated_seq)
    
    if length == 0:
        return None
    
    mid_index = length // 2
    is_even_length = (length % 2 == 0)
    
    if is_even_length:
        return (validated_seq[mid_index - 1], validated_seq[mid_index])
    else:
        return validated_seq[mid_index]

if __name__ == '__main__':
    sample_sequence_1 = [7, 8, 9, 10, 11]
    sample_sequence_2 = [25, 50, 75, 100]
    sample_sequence_3 = []
    print(get_central_item(sample_sequence_1))
    print(get_central_item(sample_sequence_2))
    print(get_central_item(sample_sequence_3))