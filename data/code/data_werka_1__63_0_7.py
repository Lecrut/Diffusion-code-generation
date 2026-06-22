def retrieve_first_element(sequence):
    return sequence[0] if sequence else None

if __name__ == '__main__':
    TEST_LIST = [99, 198, 297, 396, 495]
    first_value = retrieve_first_element(TEST_LIST)
    print(first_value)