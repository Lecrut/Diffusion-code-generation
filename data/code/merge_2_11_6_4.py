def check_list_integrity(data):
    result = []
    for seq in data:
        is_valid = len(seq) > 0 and (len(set(seq)) == 1 or len(seq) <= 1)
        result.append(is_valid)
    return all(result)
if __name__ == '__main__':
    sample_data = [[1, 2], [3, 3], [], ['a', 'b'], [5]]
    if check_list_integrity(sample_data):
        print("All sub-sequences have equal values.")
    else:
        print("Some sub-sequences contain unequal values.")