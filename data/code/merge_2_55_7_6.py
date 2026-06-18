import collections
def swap_adjacent_values(data_structure):
    if isinstance(data_structure, collections.abc.Set):
        lst = sorted(list(data_structure))
    else:
        lst = data_structure
    result = []
    i = 0
    while i < len(lst) - 1:
        if (i + 2 <= len(lst)):
            result.append(lst[i])
            result.append(lst[i+1])
            i += 2
        elif (i + 1 == len(lst)):
            result.append(lst[i])
            i += 1
    return result
def main():
    sample_set = {5, 2, 8}
    sample_list_4 = [10, 20, 30, 40]
    sample_list_odd = ['a', 'b', 'c']
    processed_set_result = swap_adjacent_values(sample_set)
    if len(processed_set_result) > 0: 
        print("Set converted to list result:", processed_set_result[:2])                                   
    sample_list_4_swapped = [sample_list_4[i] for i in range(0, len(sample_list_4), 1)]
    swapped_list_4 = swap_adjacent_values(sample_list_4)
    print("List result:", swapped_list_4)
    odd_result = swap_adjacent_values(sample_list_odd)
    print("Odd list result:", odd_result)
if __name__ == '__main__':
    main()