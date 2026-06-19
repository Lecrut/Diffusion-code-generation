def compare_lengths(length1, length2):
    result = {
        'length1': length1,
        'length2': length2,
        'is_length1_greater': length1 > length2
    }
    return result

if __name__ == '__main__':
    sample_length1 = 25
    sample_length2 = 30
    result = compare_lengths(sample_length1, sample_length2)
    print(result)