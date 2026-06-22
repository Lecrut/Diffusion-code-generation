def compare_lengths(length1, length2):
    if length1 > length2:
        return {'length1': length1, 'length2': length2, 'is_length1_greater': True}
    else:
        return {'length1': length1, 'length2': length2, 'is_length1_greater': False}

if __name__ == '__main__':
    result = compare_lengths(8, 6)
    print(result)