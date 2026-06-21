def find_smallest_element(input_tuple):
    if not input_tuple:
        raise ValueError("Input tuple is empty")
    return min(input_tuple)

if __name__ == '__main__':
    sample_input = (5, 3, 9, 1, 4)
    print(find_smallest_element(sample_input))