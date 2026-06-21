def is_float_in_list(item, data_list):
    try:
        float(item)
        return item in data_list
    except ValueError:
        print(f"Error: {item} is not a valid floating-point number.")
        return False

if __name__ == '__main__':
    sample_list = [1.5, 2.5, 3.5, 4.5]
    float_to_find_present = 3.5
    float_to_find_absent = '7.0'
    
    result_present = is_float_in_list(float_to_find_present, sample_list)
    print(f"Does the list {sample_list} contain {float_to_find_present}? {result_present}")
    
    result_absent = is_float_in_list(float_to_find_absent, sample_list)
    print(f"Does the list {sample_list} contain {float_to_find_absent}? {result_absent}")