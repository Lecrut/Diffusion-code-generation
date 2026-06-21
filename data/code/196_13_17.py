def merge_lists(target_list, source_list):
    target_list += source_list

if __name__ == '__main__':
    sample1 = [7, 8]
    sample2 = [9, 10]
    merge_lists(sample1, sample2)
    print("Merged List:", sample1)