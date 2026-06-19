def calculate_length_ratio(list1, list2):
    if len(list2) == 0:
        return float('inf')
    return len(list1) / len(list2)
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [6, 7, 8]
    ratio = calculate_length_ratio(sample_list1, sample_list2)
    print(ratio)