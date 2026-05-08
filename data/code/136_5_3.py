def check_logical_criteria(item, set_a, set_b):
    condition1 = item in set_a
    condition2 = item not in set_b
    result = condition1 and condition2
    return result
if __name__ == '__main__':
    item_to_check = "apple"
    set_a_data = {"apple", "banana", "cherry"}
    set_b_data = {"banana", "date", "elderberry"}
    result1 = check_logical_criteria(item_to_check, set_a_data, set_b_data)
    print(f"Checking '{item_to_check}':")
    print(f"Is in Set A: {item_to_check in set_a_data}")
    print(f"Is not in Set B: {item_to_check not in set_b_data}")
    print(f"Result (In A AND Not in B): {result1}")
    item_to_check_2 = "banana"
    result2 = check_logical_criteria(item_to_check_2, set_a_data, set_b_data)
    print(f"\nChecking '{item_to_check_2}':")
    print(f"Is in Set A: {item_to_check_2 in set_a_data}")
    print(f"Is not in Set B: {item_to_check_2 not in set_b_data}")
    print(f"Result (In A AND Not in B): {result2}")
    item_to_check_3 = "grape"
    result3 = check_logical_criteria(item_to_check_3, set_a_data, set_b_data)
    print(f"\nChecking '{item_to_check_3}':")
    print(f"Is in Set A: {item_to_check_3 in set_a_data}")
    print(f"Is not in Set B: {item_to_check_3 not in set_b_data}")
    print(f"Result (In A AND Not in B): {result3}")