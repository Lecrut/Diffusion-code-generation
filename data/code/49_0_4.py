def compare_lengths(length1, length2):
    def is_greater(a, b):
        return a > b

    result_dict = {
        'length1': length1,
        'length2': length2,
        'is_length1_greater': is_greater(length1, length2)
    }
    return result_dict

if __name__ == '__main__':
    sample_length1 = 20
    sample_length2 = 10
    result = compare_lengths(sample_length1, sample_length2)
    print(result)