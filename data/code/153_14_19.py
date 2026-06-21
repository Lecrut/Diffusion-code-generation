def item_exists(data, target):
    return target in data

if __name__ == '__main__':
    sample_list = [10, 25, 3, 42, 15, 7]
    target_value = 42
    print(f"List: {sample_list}, Target: {target_value}")
    print(item_exists(sample_list, target_value))
    
    sample_list_2 = [1, 5, 9, 12, 3]
    target_value_2 = 100
    print(f"List: {sample_list_2}, Target: {target_value_2}")
    print(item_exists(sample_list_2, target_value_2))
    
    sample_list_3 = [5, 10, 15, 20]
    target_value_3 = 15
    print(f"List: {sample_list_3}, Target: {target_value_3}")
    print(item_exists(sample_list_3, target_value_3))