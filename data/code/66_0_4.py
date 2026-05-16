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
    print(compare_adjacent(sample_list1))
    sample_list2 = [1, 3, 2, 4, 5]
    print(compare_adjacent(sample_list2))
    sample_list3 = [10, 5, 8, 1]
    print(compare_adjacent(sample_list3))
    sample_list4 = [7, 7, 7, 7]
    print(compare_adjacent(sample_list4))
    sample_list5 = [1, 10, 5, 20]
    print(compare_adjacent(sample_list5))