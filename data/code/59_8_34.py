def find_middle_item(sequence):
    if not sequence:
        raise ValueError("The sequence is empty")
    
    middle_index = len(sequence) // 2
    
    return sequence[middle_index]

if __name__ == '__main__':
    sample_sequence = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    try:
        middle_item = find_middle_item(sample_sequence)
        print(middle_item)
    except ValueError as e:
        print(e)