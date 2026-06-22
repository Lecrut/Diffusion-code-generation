def retrieve_elements(sequence):
    if not sequence:
        return ()
    
    first = sequence[0]
    last = sequence[-1]
    middle_index = len(sequence) // 2
    middle = sequence[middle_index]
    
    return (first, last, middle)

if __name__ == '__main__':
    example_list = [3, 6, 9, 12, 15, 18, 21]
    result = retrieve_elements(example_list)
    print(result)