def calculate_length_ratio(list1, list2):
    length1 = len(list1)
    length2 = len(list2)
    if length2 == 0:
        return float('inf')
    return length1 / length2

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [6, 7, 8]
    result = calculate_length_ratio(sample_list1, sample_list2)
    print(result)