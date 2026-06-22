def get_central_item(sequence):
    if not sequence:
        return None
    length = len(sequence)
    index = length // 2
    return sequence[index]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (10, 20, 30, 40, 50)
    sample_string = 'hello'
    sample_empty = []
    print(get_central_item(sample_list))
    print(get_central_item(sample_tuple))
    print(get_central_item(sample_string))
    print(get_central_item(sample_empty))