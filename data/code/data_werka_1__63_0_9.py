def retrieve_first_element(sequence):
    if not sequence:
        return None
    return sequence[0]

if __name__ == '__main__':
    test_list = [9, 18, 27, 36, 45]
    first_entry = retrieve_first_element(test_list)
    print(first_entry)