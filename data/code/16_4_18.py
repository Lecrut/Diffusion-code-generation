def get_first_element(sequence):
    if len(sequence) == 0:
        raise IndexError("Cannot get first element from an empty sequence")
    return sequence[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result = get_first_element(sample_list)
    print(result)
    
    try:
        empty_list = []
        get_first_element(empty_list)
    except IndexError as e:
        print(f"Caught expected error: {e}")