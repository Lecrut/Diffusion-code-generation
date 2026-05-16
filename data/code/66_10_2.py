def compare_adjacent(numbers):
    if len(numbers) < 2:
        return []
    result = []
    for i in range(len(numbers) - 1):
        if numbers[i] <= numbers[i+1]:
            result.append(True)
        else:
            result.append(False)
    return result
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [5, 4, 3, 2, 1]
    sample_list3 = [1, 3, 2, 5, 4]
    sample_list4 = [10, 20, 30]
    sample_list5 = [7, 7, 8, 9]
    sample_list6 = [1]
    sample_list7 = []
    print(f"List: {sample_list1}, Result: {compare_adjacent(sample_list1)}")
    print(f"List: {sample_list2}, Result: {compare_adjacent(sample_list2)}")
    print(f"List: {sample_list3}, Result: {compare_adjacent(sample_list3)}")
    print(f"List: {sample_list4}, Result: {compare_adjacent(sample_list4)}")
    print(f"List: {sample_list5}, Result: {compare_adjacent(sample_list5)}")
    print(f"List: {sample_list6}, Result: {compare_adjacent(sample_list6)}")
    print(f"List: {sample_list7}, Result: {compare_adjacent(sample_list7)}")