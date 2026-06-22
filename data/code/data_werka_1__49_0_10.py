def compare_lengths(length1, length2):
    comparison_table = {
        'length1': length1,
        'length2': length2
    }
    comparison_table['is_length1_greater'] = (length1 > length2)
    return comparison_table

if __name__ == '__main__':
    result = compare_lengths(8, 4)
    print(result)