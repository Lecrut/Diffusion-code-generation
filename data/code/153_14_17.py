def contains_target(data, target):
    return target in data

if __name__ == '__main__':
    sample_list = [10, 25, 3, 42, 15, 7]
    target_value = 42
    result1 = contains_target(sample_list, target_value)
    print(f"List: {sample_list}, Target: {target_value}, Found: {result1}")
    
    sample_list_2 = [1, 5, 9, 12, 3]
    target_value_2 = 100
    result2 = contains_target(sample_list_2, target_value_2)
    print(f"List: {sample_list_2}, Target: {target_value_2}, Found: {result2}")
    
    sample_list_3 = [5, 10, 15, 20]
    target_value_3 = 15
    result3 = contains_target(sample_list_3, target_value_3)
    print(f"List: {sample_list_3}, Target: {target_value_3}, Found: {result3}")