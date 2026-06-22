def retrieve_final_item(sequence):
    last_index = -1
    final_value = sequence[last_index]
    return final_value

if __name__ == '__main__':
    test_data = ['alpha', 'bravo', 'charlie', 'delta']
    extracted_item = retrieve_final_item(test_data)
    print(extracted_item)