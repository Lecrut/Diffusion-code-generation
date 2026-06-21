def get_middle(seq):
    length = len(seq)
    if length == 0:
        raise ValueError("Sequence must not be empty")
    mid_index = length // 2
    if length % 2 == 0:
        left = seq[mid_index - 1]
        right = seq[mid_index]
        avg_sum = left + right
        if isinstance(avg_sum, (int, float)) and (avg_sum % 2) == 0:
            return avg_sum / 2
        return avg_sum / 2.0
    return seq[mid_index]

if __name__ == '__main__':
    list_result = get_middle([1, 2, 3])
    print(list_result)
    string_result = get_middle("python")
    print(string_result)
    tuple_result = get_middle((10, 20, 30, 40, 50))
    print(tuple_result)
    single_result = get_middle([99])
    print(single_result)
    even_list_result = get_middle([10, 20])
    print(even_list_result)