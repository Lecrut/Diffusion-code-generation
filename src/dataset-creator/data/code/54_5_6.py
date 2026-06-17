def find_middle_index(collection):
    if not collection:
        return None
    length = len(collection)
    if length % 2 == 1:
        middle_index = (length - 1) // 2
    else:
        lower_mid = (length - 1) // 2
        upper_mid = lower_mid + 1
        return (lower_mid + upper_mid) // 2
    return int(middle_index)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = find_middle_index(sample_list)
    print(result)