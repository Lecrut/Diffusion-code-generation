def check_adjacent_increasing(numbers):
    results = []
    for i in range(len(numbers) - 1):
        if numbers[i+1] > numbers[i]:
            results.append(True)
        else:
            results.append(False)
    return results
if __name__ == '__main__':
    sample_list1 = [1.0, 2.5, 3.0, 1.5, 4.0]
    sample_list2 = [5.0, 5.0, 6.0, 7.0]
    sample_list3 = [10.0, 9.0, 8.0]
    sample_list4 = [1.1, 1.1, 1.1]
    sample_list5 = [1.0, 2.0]
    sample_list6 = []
    sample_list7 = [5.0]
    print(check_adjacent_increasing(sample_list1))
    print(check_adjacent_increasing(sample_list2))
    print(check_adjacent_increasing(sample_list3))
    print(check_adjacent_increasing(sample_list4))
    print(check_adjacent_increasing(sample_list5))
    print(check_adjacent_increasing(sample_list6))
    print(check_adjacent_increasing(sample_list7))