def compare_adjacent(data):
    result = []
    for i in range(len(data) - 1):
        if data[i] <= data[i + 1]:
            result.append(True)
        else:
            result.append(False)
    return result

if __name__ == '__main__':
    sample_list1 = [3, 5, 7, 9]
    sample_list2 = [9, 8, 7, 6]
    sample_list3 = [1, 4, 2, 3]
    sample_list4 = [10, 10, 10]
    sample_list5 = [2, 2, 3, 3, 4]
    print(f"List: {sample_list1}, Result: {compare_adjacent(sample_list1)}")
    print(f"List: {sample_list2}, Result: {compare_adjacent(sample_list2)}")
    print(f"List: {sample_list3}, Result: {compare_adjacent(sample_list3)}")
    print(f"List: {sample_list4}, Result: {compare_adjacent(sample_list4)}")
    print(f"List: {sample_list5}, Result: {compare_adjacent(sample_list5)}")