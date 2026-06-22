def compare_lengths(length1, length2):
    def determine_greater(l1, l2):
        return l1 > l2

    lengths = {
        'length1': length1,
        'length2': length2
    }
    lengths['is_length1_greater'] = determine_greater(length1, length2)
    return lengths

if __name__ == '__main__':
    result = compare_lengths(15, 9)
    print(result)