def check_logical_criteria(item, set_a, set_b):
    condition1 = item in set_a
    condition2 = item not in set_b
    result = condition1 and condition2
    return result
if __name__ == '__main__':
    item_to_check = "apple"
    set_a = {"apple", "banana", "cherry"}
    set_b = {"banana", "date", "elderberry"}
    result1 = check_logical_criteria(item_to_check, set_a, set_b)
    print(f"Checking '{item_to_check}':")
    print(f"Is in set A: {item_to_check in set_a}")
    print(f"Is not in set B: {item_to_check not in set_b}")
    print(f"Result (in A AND not in B): {result1}")
    item_to_check_2 = "banana"
    result2 = check_logical_criteria(item_to_check_2, set_a, set_b)
    print(f"\nChecking '{item_to_check_2}':")
    print(f"Is in set A: {item_to_check_2 in set_a}")
    print(f"Is not in set B: {item_to_check_2 not in set_b}")
    print(f"Result (in A AND not in B): {result2}")
    item_to_check_3 = "grape"
    result3 = check_logical_criteria(item_to_check_3, set_a, set_b)
    print(f"\nChecking '{item_to_check_3}':")
    print(f"Is in set A: {item_to_check_3 in set_a}")
    print(f"Is not in set B: {item_to_check_3 not in set_b}")
    print(f"Result (in A AND not in B): {result3}")