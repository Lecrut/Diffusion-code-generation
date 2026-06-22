def find_final_index(data_list, target_item):
    if not isinstance(data_list, list):
        raise ValueError("data_list must be a list")
    
    last_index = -1
    for index, item in enumerate(reversed(data_list)):
        if item == target_item:
            last_index = len(data_list) - 1 - index
            break
    
    return last_index

if __name__ == '__main__':
    try:
        sample_data1 = [1, 2, 3, 2, 4, 2, 5]
        target1 = 2
        result1 = find_final_index(sample_data1, target1)
        print(f"List: {sample_data1}, Target: {target1}, Final Index: {result1}")

        sample_data2 = ['a', 'b', 'c', 'b', 'd', 'b']
        target2 = 'b'
        result2 = find_final_index(sample_data2, target2)
        print(f"List: {sample_data2}, Target: {target2}, Final Index: {result2}")

        sample_data3 = [10, 20, 30, 40]
        target3 = 5
        result3 = find_final_index(sample_data3, target3)
        print(f"List: {sample_data3}, Target: {target3}, Final Index: {result3}")

    except ValueError as e:
        print(e)