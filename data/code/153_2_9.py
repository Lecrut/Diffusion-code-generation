def contains_float(item, data_list):
    return any(isinstance(i, float) and i == item for i in data_list)

if __name__ == '__main__':
    sample_list = [1.5, 2, 3.7, 4]
    item_to_find_present = 3.7
    item_to_find_absent = 5
    result_present = contains_float(item_to_find_present, sample_list)
    result_absent = contains_float(item_to_find_absent, sample_list)
    print(f"Does the list {sample_list} contain {item_to_find_present}? {result_present}")
    print(f"Does the list {sample_list} contain {item_to_find_absent}? {result_absent}")