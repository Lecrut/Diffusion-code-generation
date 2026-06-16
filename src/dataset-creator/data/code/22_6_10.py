def delete_by_index(sequence: any, index: int) -> any:
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
    sample_index_str = 7
    delete_char_from_string = delete_by_index(sample_string, int(sample_index_str))
    print(delete_char_from_string)