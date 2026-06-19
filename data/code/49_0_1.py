def compare_lengths(length1, length2):
    return {
        'length1': length1,
        'length2': length2,
        'is_length1_greater': length1 > length2
    }

if __name__ == '__main__':
    result = compare_lengths(10, 5)
    print(result)