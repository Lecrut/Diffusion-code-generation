def extract_penultimate(data_sequence):
    sequence_length = len(data_sequence)
    if sequence_length < 2:
        raise IndexError("Input must contain at least two items")
    target_index = -2
    extracted_value = data_sequence[target_index]
    return extracted_value

if __name__ == '__main__':
    test_collection = [5, 15, 25, 35, 45]
    retrieved_item = extract_penultimate(test_collection)
    print(retrieved_item)