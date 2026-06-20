def compare_lengths_meters_to_cm(len1, len2):
    len1_cm = len1 * 100
    len2_cm = len2 * 100
    if len1_cm >= len2_cm:
        return len1
    else:
        return len2

if __name__ == '__main__':
    sample_len1 = 1.5
    sample_len2 = 2.0
    result = compare_lengths_meters_to_cm(sample_len1, sample_len2)
    print(result)