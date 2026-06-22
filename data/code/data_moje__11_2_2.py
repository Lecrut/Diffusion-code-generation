def retrieve_tail_element(data_set):
    extracted_tail = data_set[-1:]
    return extracted_tail[0]

if __name__ == '__main__':
    test_collection = ["alpha", "bravo", "charlie", "delta", "echo"]
    final_item = retrieve_tail_element(test_collection)
    print(final_item)