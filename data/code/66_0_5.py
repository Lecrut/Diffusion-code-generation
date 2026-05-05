def compare_adjacent(numbers):
    result = []
    for i in range(len(numbers) - 1):
        if numbers[i] <= numbers[i+1]:
            result.append(True)
        else:
            result.append(False)
    return result
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [1, 3, 2, 4, 5]
    sample_list3 = [10, 5, 15, 12]
    sample_list4 = [7, 7, 8, 9]
    sample_list5 = [1, 1, 1, 1]
    print(f"List: {sample_list1}, Result: {compare_adjacent(sample_list1)}")
    print(f"List: {sample_list2}, Result: {compare_adjacent(sample_list2)}")
    print(f"List: {sample_list3}, Result: {compare_adjacent(sample_list3)}")
    print(f"List: {sample_list4}, Result: {compare_adjacent(sample_list4)}")
    print(f"List: {sample_list5}, Result: {compare_adjacent(sample_list5)}")