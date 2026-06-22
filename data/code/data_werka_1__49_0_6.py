def compare_lengths(length1, length2):
    comparison_map = {
        'length1': length1,
        'length2': length2
    }
    comparison_map['is_length1_greater'] = comparison_map['length1'] > comparison_map['length2']
    return comparison_map

if __name__ == '__main__':
    result = compare_lengths(8, 6)
    print(result)