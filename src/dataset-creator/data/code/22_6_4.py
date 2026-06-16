def delete_by_index(sequence, index):
    if isinstance(sequence, str):
        return sequence[:index] + sequence[index+1:]
    elif isinstance(sequence, list):
        new_list = []
        for i in range(len(sequence)):
            if i != index:
                new_list.append(sequence[i])
        return new_list
    else:
        raise TypeError("Input must be a string or a list.")
if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_list = [10, 20, 30, 40]
    char_to_delete_index = 7
    result_str = delete_by_index(sample_string, char_to_delete_index)
    print(f"String after deletion: {result_str}")
    item_to_delete_index = 2
    result_list = delete_by_index(sample_list, item_to_delete_index)
    print(f"List after deletion: {result_list}")