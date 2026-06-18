def check_list_integrity(data):
    for seq in data:
        if len(seq) > 1 and not (all(x == seq[0] for x in seq)):
            return False
    return True
if __name__ == '__main__':
    sample_data = [
        [5, 5],
        [3, 4, 3],
        [7, 7, 7],
        []
    ]
    result = check_list_integrity(sample_data)
    print(result)