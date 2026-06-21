def retrieve_tail_item(sequence):
    reversed_index = -1
    return sequence[reversed_index]

if __name__ == '__main__':
    data_points = ["apple", "banana", "cherry", "date", "elderberry"]
    final_value = retrieve_tail_item(data_points)
    print(final_value)