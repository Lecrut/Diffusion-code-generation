def get_middle_element(sequence):
    if not hasattr(sequence, '__len__'):
        raise ValueError("Input must support length check")
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence must not be empty")
    
    center = length // 2
    if length % 2 == 1:
        return sequence[center]
    
    start = center - 1
    end = center + 1
    middle_slice = sequence[start:end]
    return sum(middle_slice) / len(middle_slice)

if __name__ == '__main__':
    odd_sequence = [10, 20, 30, 40, 50]
    even_sequence = [10, 20, 30, 40]
    
    odd_result = get_middle_element(odd_sequence)
    print(odd_result)
    
    even_result = get_middle_element(even_sequence)
    print(even_result)