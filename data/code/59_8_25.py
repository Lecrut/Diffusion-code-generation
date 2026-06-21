def validate_sequence(sequence):
    if not sequence:
        raise ValueError("The sequence is empty")

def find_middle_item(sequence):
    validate_sequence(sequence)
    middle_index = len(sequence) // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_list = [7, 8, 9, 10, 11]
    print(find_middle_item(sample_list))