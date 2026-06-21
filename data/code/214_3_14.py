def find_smallest_element(input_tuple):
    if not input_tuple:
        raise ValueError('Input tuple is empty')
    return min(input_tuple)
if __name__ == '__main__':
    sample_tuple = (5, 3, 9, 1, 4)
    try:
        result = find_smallest_element(sample_tuple)
        print(result)
    except ValueError as e:
        print(e)