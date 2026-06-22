def compare_lengths(length1, length2):
    comparison_map = {
        'length1': length1,
        'length2': length2,
        'is_length1_greater': None
    }
    
    def determine_greater(l1, l2):
        return l1 > l2
    
    comparison_map['is_length1_greater'] = determine_greater(length1, length2)
    return comparison_map

if __name__ == '__main__':
    sample_length1 = 25
    sample_length2 = 30
    result = compare_lengths(sample_length1, sample_length2)
    print(result)