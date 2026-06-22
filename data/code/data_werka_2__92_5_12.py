def negate_boolean_sequence(data_stream):
    result_buffer = []
    for element in data_stream:
        if type(element) is not bool:
            raise ValueError(f"Expected bool, got {type(element)}")
        result_buffer.append(not element)
    return result_buffer

if __name__ == '__main__':
    input_sequence = [True, False, True, True, False]
    inverted_sequence = negate_boolean_sequence(input_sequence)
    print(inverted_sequence)