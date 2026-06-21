def contains_floating_point(item, data_list):
    try:
        return any(abs(item - num) < 1e-9 for num in data_list)
    except TypeError:
        return False

if __name__ == '__main__':
    sample_list = [1.0, 5.5, 10.3, 15.2, 20.7]
    item_to_find_present = 10.3
    item_to_find_absent = '10'
    result_present = contains_floating_point(item_to_find_present, sample_list)
    result_absent = contains_floating_point(item_to_find_absent, sample_list)
    print(f"Does the list {sample_list} contain {item_to_find_present}? {result_present}")
    print(f"Does the list {sample_list} contain {item_to_find_absent}? {result_absent}")