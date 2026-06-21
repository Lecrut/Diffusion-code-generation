def extract_elements(sequence):
    if not sequence:
        return ()
    
    first = sequence[0]
    last = sequence[-1]
    middle_index = len(sequence) // 2
    middle = sequence[middle_index]
    
    return (first, last, middle)

if __name__ == '__main__':
    sample_data = [9, 18, 27, 36, 45, 54, 63]
    result_tuple = extract_elements(sample_data)
    print(result_tuple)