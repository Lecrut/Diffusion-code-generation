def retrieve_first_element(sequence):
    return sequence[0] if sequence else None

if __name__ == '__main__':
    TEST_LIST = [99, 88, 77, 66, 55]
    first_value = retrieve_first_element(TEST_LIST)
    print(first_value)