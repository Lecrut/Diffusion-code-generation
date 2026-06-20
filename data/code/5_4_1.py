def analyze_length_lists(list1, list2):
    combined = list1 + list2
    max_length = max(combined)
    min_length = min(combined)
    range_diff = max_length - min_length
    return max_length, min_length, range_diff

if __name__ == '__main__':
    sample_list1 = [10.5, 20.3, 15.7, 30.1]
    sample_list2 = [12.0, 25.6, 18.9, 22.4]
    result = analyze_length_lists(sample_list1, sample_list2)
    print(result)