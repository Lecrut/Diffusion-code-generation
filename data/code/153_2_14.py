def contains_floating_point(item, data_list):
    return isinstance(item, float) and item in data_list

if __name__ == '__main__':
    sample_list = [1.5, 2.5, 3.5, 4.5]
    item_to_find_present = 2.5
    item_to_find_absent = 2
    result_present = contains_floating_point(item_to_find_present, sample_list)
    result_absent = contains_floating_point(item_to_find_absent, sample_list)
    print(f"Does the list {sample_list} contain {item_to_find_present}? {result_present}")
    print(f"Does the list {sample_list} contain {item_to_find_absent}? {result_absent}")