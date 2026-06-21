def get_last_element(sequence):
    negative_index = -1
    final_item = sequence[negative_index]
    return final_item

if __name__ == '__main__':
    test_data = [100, 200, 300, 400]
    output = get_last_element(test_data)
    print(output)