def partition_and_sort_by_parity(input_list):
    parity_map = {0: [], 1: []}
    for number in input_list:
        parity_map[number % 2].append(number)
    sorted_lists = [sorted(parity_map[parity], reverse=True) for parity in [0, 1]]
    return sorted_lists
if __name__ == '__main__':
    sample_list_1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result_1 = partition_and_sort_by_parity(sample_list_1)
    print(f'Original List 1: {sample_list_1}')
    print(f'Sorted Even List 1: {result_1[0]}')
    print(f'Sorted Odd List 1: {result_1[1]}\n')
    sample_list_2 = [8, 6, 7, 5, 3, 0, 9]
    result_2 = partition_and_sort_by_parity(sample_list_2)
    print(f'Original List 2: {sample_list_2}')
    print(f'Sorted Even List 2: {result_2[0]}')
    print(f'Sorted Odd List 2: {result_2[1]}\n')
    sample_list_3 = [2, 4, 6, 8]
    result_3 = partition_and_sort_by_parity(sample_list_3)
    print(f'Original List 3: {sample_list_3}')
    print(f'Sorted Even List 3: {result_3[0]}')
    print(f'Sorted Odd List 3: {result_3[1]}\n')
    sample_list_4 = [1, 3, 5, 7]
    result_4 = partition_and_sort_by_parity(sample_list_4)
    print(f'Original List 4: {sample_list_4}')
    print(f'Sorted Even List 4: {result_4[0]}')
    print(f'Sorted Odd List 4: {result_4[1]}\n')
    sample_list_5 = []
    result_5 = partition_and_sort_by_parity(sample_list_5)
    print(f'Original List 5: {sample_list_5}')
    print(f'Sorted Even List 5: {result_5[0]}')
    print(f'Sorted Odd List 5: {result_5[1]}\n')