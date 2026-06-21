def get_third_element(sequence):
    sequence_list = list(sequence)
    if len(sequence_list) < 3:
        raise IndexError("Sequence must have at least three elements")
    return sequence_list[2]

if __name__ == '__main__':
    result = get_third_element([10, 20, 30, 40, 50])
    print(result)
    result = get_third_element("abcdef")
    print(result)
    result = get_third_element((100, 200, 300))
    print(result)