def compare_lengths(length1, length2):
    lengths = {
        'length1': length1,
        'length2': length2
    }
    lengths['is_length1_greater'] = lengths['length1'] > lengths['length2']
    return lengths

if __name__ == '__main__':
    result = compare_lengths(7, 3)
    print(result)