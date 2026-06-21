def extract_middle_item(array):
    if not array:
        return None
    middle_index = len(array) // 2
    return array[middle_index]

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    result = extract_middle_item(sample_data)
    print(result)