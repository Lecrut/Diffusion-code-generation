def find_target_index(data, target):
    for i, value in enumerate(data):
        if value == target:
            return {"found": True, "index": i}
    return {"found": False}
if __name__ == '__main__':
    sample_list = [10, 5, 20, 15, 30]
    target_value = 15
    result1 = find_target_index(sample_list, target_value)
    print(f"List: {sample_list}, Target: {target_value}")
    print(result1)
    sample_list_2 = [1, 2, 3, 4, 5]
    target_value_2 = 99
    result2 = find_target_index(sample_list_2, target_value_2)
    print(f"List: {sample_list_2}, Target: {target_value_2}")
    print(result2)
    sample_list_3 = [7, 7, 7, 7]
    target_value_3 = 7
    result3 = find_target_index(sample_list_3, target_value_3)
    print(f"List: {sample_list_3}, Target: {target_value_3}")
    print(result3)