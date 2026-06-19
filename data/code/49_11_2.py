def calculate_lengths(length1, length2):
    lengths = {
        'length1': length1,
        'length2': length2,
        'difference': abs(length1 - length2),
        'ratio': max(length1, length2) / min(length1, length2)
    }
    return lengths

if __name__ == '__main__':
    sample_length1 = 10
    sample_length2 = 5
    result = calculate_lengths(sample_length1, sample_length2)
    print(result)