def find_final_index(data_list, target_item):
    def validate_input():
        if not isinstance(data_list, list):
            raise ValueError("The data_list must be a list.")
        if not isinstance(target_item, (int, str, float, bool)):
            raise ValueError("The target_item must be an int, str, float, or bool.")

    validate_input()
    last_index = -1
    for index, item in enumerate(data_list):
        if item == target_item:
            last_index = index
    return last_index

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 40]
    target = 40
    result = find_final_index(sample_data, target)
    print(f"List: {sample_data}, Target: {target}, Final Index: {result}")

    sample_data2 = ['apple', 'banana', 'cherry', 'date', 'banana']
    target2 = 'banana'
    result2 = find_final_index(sample_data2, target2)
    print(f"List: {sample_data2}, Target: {target2}, Final Index: {result2}")

    sample_data3 = [True, False, True, False]
    target3 = True
    result3 = find_final_index(sample_data3, target3)
    print(f"List: {sample_data3}, Target: {target3}, Final Index: {result3}")