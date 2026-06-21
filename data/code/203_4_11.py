def count_greater_elements(list1, list2):
    return sum(1 for a, b in zip(list1, list2) if a > b)

if __name__ == '__main__':
    sample_list1 = [5, 3, 9, 7]
    sample_list2 = [4, 3, 8, 6]
    print(count_greater_elements(sample_list1, sample_list2))