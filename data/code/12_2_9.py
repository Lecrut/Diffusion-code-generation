def get_central_item(sequence):
    if not sequence:
        raise ValueError("Sequence must not be empty")
    n = len(sequence)
    if n % 2 == 0:
        mid = n // 2
        return sequence[mid - 1]
    else:
        return sequence[n // 2]

if __name__ == '__main__':
    list_seq = [1, 2, 3, 4, 5]
    print(get_central_item(list_seq))
    tuple_seq = (10, 20, 30, 40)
    print(get_central_item(tuple_seq))
    string_seq = "abcde"
    print(get_central_item(string_seq))
    single_item = [99]
    print(get_central_item(single_item))