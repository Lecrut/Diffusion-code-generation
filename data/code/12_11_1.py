def get_middle_element(sequence):
    if not sequence:
        raise ValueError("Cannot find the middle element of an empty sequence.")
    
    middle_index = len(sequence) // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    result = get_middle_element(sample_tuple)
    print(result)
    
    empty_tuple = ()
    try:
        get_middle_element(empty_tuple)
    except ValueError as e:
        print(f"Caught expected error: {e}")