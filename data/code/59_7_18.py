def is_sequence_empty(sequence):
    return len(sequence) == 0

def calculate_middle_index(n):
    return n // 2

def find_middle(sequence):
    if is_sequence_empty(sequence):
        raise ValueError('Sequence cannot be empty')
    middle_index = calculate_middle_index(len(sequence))
    return sequence[middle_index]
if __name__ == '__main__':
    sample_sequence_odd = [1, 2, 3, 4, 5]
    sample_sequence_even = [10, 20, 30, 40, 50, 60]
    print(find_middle(sample_sequence_odd))
    print(find_middle(sample_sequence_even))