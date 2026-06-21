def count_greater_elements(list1, list2):
    return sum(1 for a, b in zip(list1, list2) if a > b)

if __name__ == '__main__':
    sample_list1 = [3, 5, 2, 8]
    sample_list2 = [1, 4, 3, 7]
    print(count_greater_elements(sample_list1, sample_list2))