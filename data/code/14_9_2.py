import threading

safe_counter = threading.Lock()

def get_third_element(data_list, default_value):
    if len(data_list) >= 3:
        return data_list[2]
    return default_value

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    short_list = [1, 2]
    default = "Not Found"
    
    with safe_counter:
        result_long = get_third_element(sample_list, default)
        result_short = get_third_element(short_list, default)
    
    print(result_long)
    print(result_short)