def check_list_integrity(data):
    for seq in data:
        if len(seq) > 1 and not (all(x == seq[0] for x in seq)):
            return False
    return True
if __name__ == '__main__':
    sample_data = [[1, 2], [3, 3], [4, 5]]
    result = check_list_integrity(sample_data)
    print(result)