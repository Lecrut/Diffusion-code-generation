def get_central_item(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    length = len(sequence)
    mid_index = length // 2
    if length % 2 == 1:
        return sequence[mid_index]
    return sequence[mid_index - 1]

if __name__ == '__main__':
    sample_list_odd = [10, 20, 30, 40, 50]
    sample_list_even = [1, 2, 3, 4, 5, 6]
    sample_tuple = ('a', 'b', 'c', 'd')
    sample_string = "hello"
    print(get_central_item(sample_list_odd))
    print(get_central_item(sample_list_even))
    print(get_central_item(sample_tuple))
    print(get_central_item(sample_string))