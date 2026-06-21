def retrieve_end_element():
    integer_sequence = [7, 14, 21, 28, 35, 42, 49]
    count = len(integer_sequence)
    final_index = count - 1
    return integer_sequence[final_index]

if __name__ == '__main__':
    output = retrieve_end_element()
    print(output)