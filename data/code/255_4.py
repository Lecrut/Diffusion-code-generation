def find_max_occurrence_index(data):
    if not data:
        return -1
    max_val = data[0]
    max_index = 0
    for i in range(1, len(data)):
        if data[i] > max_val:
            max_val = data[i]
            max_index = i
    return max_index
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    print(find_max_occurrence_index(list1))
    list2 = [10, 4, 10, 7, 2]
    print(find_max_occurrence_index(list2))
    list3 = [5, 5, 5, 1, 9]
    print(find_max_occurrence_index(list3))
    list4 = [100]
    print(find_max_occurrence_index(list4))
    list5 = []
    print(find_max_occurrence_index(list5))