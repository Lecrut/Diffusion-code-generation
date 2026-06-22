def get_central_item(sequence):
    if not sequence:
        return None
    length = len(sequence)
    mid_index = length // 2
    if length % 2 == 0:
        return (sequence[mid_index - 1] + sequence[mid_index]) / 2
    else:
        return sequence[mid_index]
if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    sample_tuple = (2, 4, 6, 8)
    sample_string = 'hello'
    print(get_central_item(sample_list))
    print(get_central_item(sample_tuple))
    print(get_central_item(sample_string))