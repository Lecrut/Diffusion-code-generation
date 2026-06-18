def check_list_integrity(data):
    for sequence in data:
        if len(sequence) == 0:
            continue
        first_value = sequence[0]
        for value in sequence[1:]:
            if value != first_value:
                return False
    return True
if __name__ == '__main__':
    sample_data = [
        [1, 1, 1],
        [2, 2],
        [],
        [3, 4]
    ]
    result = check_list_integrity(sample_data)
    print(result)