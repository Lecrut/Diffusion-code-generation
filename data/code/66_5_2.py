def check_adjacent_increasing(numbers):
    result = []
    for i in range(len(numbers) - 1):
        if numbers[i+1] > numbers[i]:
            result.append(True)
        else:
            result.append(False)
    return result
if __name__ == '__main__':
    sample_list1 = [1.0, 2.5, 3.0, 1.5]
    sample_list2 = [5.0, 5.0, 6.0, 7.0]
    sample_list3 = [10.1, 10.1, 10.2]
    sample_list4 = [1.0, 0.5, 2.0]
    sample_list5 = [3.3, 3.3, 3.3]
    print(check_adjacent_increasing(sample_list1))
    print(check_adjacent_increasing(sample_list2))
    print(check_adjacent_increasing(sample_list3))
    print(check_adjacent_increasing(sample_list4))
    print(check_adjacent_increasing(sample_list5))