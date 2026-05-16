def check_logical_criteria(item, set_a, set_b):
    condition_a = item in set_a
    condition_b = item not in set_b
    result = condition_a and condition_b
    return result
if __name__ == '__main__':
    item_to_check = "apple"
    set_a = {"apple", "banana", "cherry"}
    set_b = {"banana", "date", "elderberry"}
    result1 = check_logical_criteria(item_to_check, set_a, set_b)
    print(f"Checking '{item_to_check}': In set A ({set_a}) AND Not in set B ({set_b}) -> {result1}")
    item_to_check_2 = "banana"
    result2 = check_logical_criteria(item_to_check_2, set_a, set_b)
    print(f"Checking '{item_to_check_2}': In set A ({set_a}) AND Not in set B ({set_b}) -> {result2}")
    item_to_check_3 = "grape"
    result3 = check_logical_criteria(item_to_check_3, set_a, set_b)
    print(f"Checking '{item_to_check_3}': In set A ({set_a}) AND Not in set B ({set_b}) -> {result3}")