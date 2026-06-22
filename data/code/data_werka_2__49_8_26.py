def compare_lengths(length1, length2):
    lengths = [length1, length2]
    return (min(lengths), max(lengths))

if __name__ == '__main__':
    sample_length1 = 35
    sample_length2 = 40
    result = compare_lengths(sample_length1, sample_length2)
    print(result)