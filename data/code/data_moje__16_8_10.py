FIRST_ELEMENT_INDEX = 0

DEFAULT_DATA_SET = [55, 66, 77, 88, 99]

def retrieve_initial_element(input_sequence=None):
    if input_sequence is None:
        source_vector = DEFAULT_DATA_SET
    else:
        source_vector = input_sequence
    index_pointer = FIRST_ELEMENT_INDEX
    initial_item = source_vector[index_pointer]
    return initial_item

if __name__ == '__main__':
    test_data = [101, 202, 303]
    found_value = retrieve_initial_element(test_data)
    print(found_value)