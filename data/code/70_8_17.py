def check_endpoints(data_source):
    endpoint_container = list(data_source)
    total_items = len(endpoint_container)
    if total_items == 0:
        return None, None
    start_value = endpoint_container[0]
    end_value = endpoint_container[-1]
    return start_value, end_value

if __name__ == '__main__':
    test_data = [10, 20, 30, 40, 50]
    initial, final = check_endpoints(test_data)
    print(initial, final)
    empty_data = []
    e_initial, e_final = check_endpoints(empty_data)
    print(e_initial, e_final)
    single_data = [99]
    s_initial, s_final = check_endpoints(single_data)
    print(s_initial, s_final)