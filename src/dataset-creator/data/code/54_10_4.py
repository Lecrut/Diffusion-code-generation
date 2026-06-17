def find_middle_index(lst):
    if not lst:
        return None
    length = len(lst)
    if length % 2 == 1:
        middle_index = length // 2
        return middle_index
    else:
        first_half_length = (length - 1) // 2
        return first_half_length
if __name__ == '__main__':
    sample_list = [0, 1, 2, 3]
    result = find_middle_index(sample_list)
    print(result if result is not None else "Empty list")