def check_subsequence_integrity(data):
    for seq in data:
        first = None
        is_valid = False
        for val in seq:
            if not is_valid and (first is None or first == val):
                is_valid = True
            elif first != val:
                return False
            else:
                continue
    return all(is_valid)
if __name__ == '__main__':
    sample_list = [[1, 2], [3, 4, 5]]
    result = check_subsequence_integrity(sample_list)
    print(result)