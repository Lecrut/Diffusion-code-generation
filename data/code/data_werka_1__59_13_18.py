def get_central_item(sequence):
    if not sequence:
        return None
    length = len(sequence)
    mid_index = length // 2
    if length % 2 == 0:
        return (sequence[mid_index - 1], sequence[mid_index])
    else:
        return sequence[mid_index]
if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(get_central_item(sample_values))
    even_sample_values = [1, 2, 3, 4]
    print(get_central_item(even_sample_values))
    empty_sample_values = []
    print(get_central_item(empty_sample_values))