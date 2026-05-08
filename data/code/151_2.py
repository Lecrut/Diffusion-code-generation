list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = [x for lst in [list1, list2] for x in lst]
if __name__ == '__main__':
    print(combined_list)