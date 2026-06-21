def remove_first_occurrence(lst, num):
    if num in lst:
        lst.remove(num)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3]
    print("Original list:", sample_list)
    remove_first_occurrence(sample_list, 3)
    print("Modified list:", sample_list)