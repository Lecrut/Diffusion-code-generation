def swap_adjacent(data: tuple) -> list:
    if len(data) <= 1:
        return data
    result = []
    i = 0
    while i < len(data):
        if i + 1 < len(data):
            result.append(data[i])
            result.insert(1, data[i+1])
            i += 2
        else:
            result.append(data[i])
            break
    return list(result)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = (5, 6, 7, 8)
    print("Original List:", sample_list)
    swapped_list = swap_adjacent(sample_list)
    print("Swapped List:", swapped_list)
    print("\nOriginal Tuple:", sample_tuple)
    swapped_tuple_result = swap_adjacent(sample_tuple)
    print("Swapped Result (as list):", swapped_tuple_result)