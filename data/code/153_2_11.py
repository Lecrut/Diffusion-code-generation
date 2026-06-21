def is_float(item):
    return isinstance(item, float)

def contains_float(item, data_list):
    if not is_float(item):
        raise ValueError("Item must be a floating-point number")
    return item in data_list

if __name__ == '__main__':
    sample_list = [1.0, 5.5, 10.1, 15.2, 20.3]
    float_to_find_present = 10.1
    float_to_find_absent = 12.0
    result_present = contains_float(float_to_find_present, sample_list)
    result_absent = contains_float(float_to_find_absent, sample_list)
    print(f"Does the list {sample_list} contain {float_to_find_present}? {result_present}")
    print(f"Does the list {sample_list} contain {float_to_find_absent}? {result_absent}")