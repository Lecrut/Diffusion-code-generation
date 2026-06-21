def extend_list_in_place(list1, list2):
    list1.extend(list2)

if __name__ == '__main__':
    sample_list1 = [19, 20, 21]
    sample_list2 = [22, 23, 24]
    extend_list_in_place(sample_list1, sample_list2)
    print(sample_list1)