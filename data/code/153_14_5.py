def find_target_index(data, target):
    for i, value in enumerate(data):
        if value == target:
            return {"found": True, "index": i}
    return {"found": False}
if __name__ == '__main__':
    sample_list = [10, 25, 3, 42, 15, 88, 3]
    target_value = 42
    result1 = find_target_index(sample_list, target_value)
    print(f"List: {sample_list}, Target: {target_value}")
    print(result1)
    sample_list_2 = [1, 5, 9, 12, 3]
    target_value_2 = 100
    result2 = find_target_index(sample_list_2, target_value_2)
    print(f"List: {sample_list_2}, Target: {target_value_2}")
    print(result2)
    sample_list_3 = [5, 10, 15]
    target_value_3 = 10
    result3 = find_target_index(sample_list_3, target_value_3)
    print(f"List: {sample_list_3}, Target: {target_value_3}")
    print(result3)