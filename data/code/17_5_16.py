def get_last_element(sequence):
    sequence_length = len(sequence)
    if sequence_length == 0:
        raise IndexError("Sequence is empty")
    final_index = sequence_length - 1
    return sequence[final_index]

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    last_item = get_last_element(my_list)
    print(last_item)