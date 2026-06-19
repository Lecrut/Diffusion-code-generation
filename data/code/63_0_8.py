def retrieve_first_element(sequence):
    return sequence[0] if sequence else None

if __name__ == '__main__':
    test_list = ['apple', 'banana', 'cherry']
    first_entry = retrieve_first_element(test_list)
    print(first_entry)