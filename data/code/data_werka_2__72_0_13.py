def compare_elements(list_one, list_two, target_index):
    sentinel = object()
    val_a = sentinel
    val_b = sentinel
    if 0 <= target_index < len(list_one):
        val_a = list_one[target_index]
    if 0 <= target_index < len(list_two):
        val_b = list_two[target_index]
    if val_a is sentinel:
        val_a = "Missing"
    if val_b is sentinel:
        val_b = "Missing"
    return val_a, val_b

if __name__ == '__main__':
    source_a = [100, 200, 300, 400]
    source_b = [10, 20, 30, 40, 50]
    check_idx = 2
    first_val, second_val = compare_elements(source_a, source_b, check_idx)
    print(f"Element from first list: {first_val}")
    print(f"Element from second list: {second_val}")
    invalid_idx = 10
    missing_a, missing_b = compare_elements(source_a, source_b, invalid_idx)
    print(f"Result at invalid index: ({missing_a}, {missing_b})")