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
    deleted_char = delete_by_index(sample_string, 7)
    print(f"Deleted from string: {deleted_char}")
    deleted_item = delete_by_index(sample_list, 2)
    print(f"Deleted from list: {deleted_item}")