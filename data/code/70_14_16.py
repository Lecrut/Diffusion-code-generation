def retrieve_boundaries(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")
    if len(input_list) == 0:
        raise ValueError("List cannot be empty")
    return {
        'first': input_list[0],
        'last': input_list[-1]
    }

if __name__ == '__main__':
    sample_data = [4, 8, 15, 16, 23, 42]
    boundaries = retrieve_boundaries(sample_data)
    print(f"first={boundaries['first']}, last={boundaries['last']}")