def safe_first_element(sequence):
    if len(sequence) == 0:
        raise IndexError("sequence is empty")
    return sequence[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_empty = []
    
    result = safe_first_element(sample_list)
    print(result)
    
    try:
        safe_first_element(sample_empty)
    except IndexError as e:
        print(f"Caught exception: {e}")