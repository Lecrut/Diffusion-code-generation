def calculate_length_ratio(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    if len2 == 0:
        return float('inf') if len1 > 0 else 0.0
    return len1 / len2

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [6, 7, 8]
    ratio = calculate_length_ratio(sample_list1, sample_list2)
    print(ratio)