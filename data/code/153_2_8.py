def contains_floating_point(item, data_list):
    for element in data_list:
        if isinstance(element, float) and abs(element - item) < 1e-9:
            return True
    return False

if __name__ == '__main__':
    sample_list = [1.0, 5.0, 10.0, 15.0, 20.0]
    item_to_find_present = 10.0
    item_to_find_absent = 10.1
    result_present = contains_floating_point(item_to_find_present, sample_list)
    result_absent = contains_floating_point(item_to_find_absent, sample_list)
    print(f"Does the list {sample_list} contain {item_to_find_present}? {result_present}")
    print(f"Does the list {sample_list} contain {item_to_find_absent}? {result_absent}")