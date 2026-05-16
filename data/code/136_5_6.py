def check_criteria(item, set_a, set_b):
    condition_a = item in set_a
    condition_b = item not in set_b
    result = condition_a and condition_b
    return result
if __name__ == '__main__':
    item_to_check = "apple"
    set_a = {"apple", "banana", "cherry"}
    set_b = {"banana", "date", "elderberry"}
    result = check_criteria(item_to_check, set_a, set_b)
    print(result)