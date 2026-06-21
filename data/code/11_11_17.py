def extract_tail(collection):
    if len(collection) == 0:
        return None
    final_element = collection.pop()
    return final_element

if __name__ == '__main__':
    data_sequence = [99, 88, 77, 66, 55, 44, 33, 22, 11]
    result = extract_tail(data_sequence)
    print(result)
    empty_data = []
    result_empty = extract_tail(empty_data)
    print(result_empty)