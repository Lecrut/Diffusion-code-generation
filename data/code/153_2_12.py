def is_float_in_list(item, data_list):
    try:
        return float(item) in data_list
    except ValueError:
        return False

if __name__ == '__main__':
    sample_list = [1.0, 5.5, 10.0, 15.5, 20.0]
    item_to_find_present = '10'
    item_to_find_absent = '7'
    result_present = is_float_in_list(item_to_find_present, sample_list)
    result_absent = is_float_in_list(item_to_find_absent, sample_list)
    print(f"Does the list {sample_list} contain {item_to_find_present}? {result_present}")
    print(f"Does the list {sample_list} contain {item_to_find_absent}? {result_absent}")