def compare_adjacent(data):
    result = []
    for i in range(len(data) - 1):
        result.append(data[i] <= data[i + 1])
    return result

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [5, 4, 3, 2, 1]
    sample_list3 = [1, 3, 2, 4]
    sample_list4 = [10, 20, 30]
    sample_list5 = [7, 7, 8, 9]
    
    test_cases = {
        "Ascending": sample_list1,
        "Descending": sample_list2,
        "Mixed": sample_list3,
        "Strictly Increasing": sample_list4,
        "Equal and Increasing": sample_list5
    }
    
    for name, lst in test_cases.items():
        print(f"List: {lst}, Result: {compare_adjacent(lst)}")