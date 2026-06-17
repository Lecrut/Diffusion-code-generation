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
    list1 = [10, 5, 20, 8, 20, 15]
    list2 = [3, 3, 3, 1, 5]
    list3 = [7, 7, 7, 7]
    list4 = [50]
    list5 = []
    print(f"List: {list1}, Index of max: {find_max_occurrence_index(list1)}")
    print(f"List: {list2}, Index of max: {find_max_occurrence_index(list2)}")
    print(f"List: {list3}, Index of max: {find_max_occurrence_index(list3)}")
    print(f"List: {list4}, Index of max: {find_max_occurrence_index(list4)}")
    print(f"List: {list5}, Index of max: {find_max_occurrence_index(list5)}")