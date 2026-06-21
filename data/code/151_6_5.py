MAX_LIST_SIZE = 1000

def extend_list_in_place(list1, list2):
    if len(list1) + len(list2) > MAX_LIST_SIZE:
        raise ValueError("Combined length exceeds maximum allowed size")
    list1.extend(list2)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    extend_list_in_place(sample_list1, sample_list2)
    print(sample_list1)