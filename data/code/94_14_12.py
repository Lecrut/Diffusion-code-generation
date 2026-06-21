def verify_true_present(bool_list):
    status_map = {True: 1, False: 0}
    active_indicators = 0
    for item in bool_list:
        active_indicators += status_map.get(item, 0)
    return active_indicators > 0

if __name__ == '__main__':
    data_set = [False, False, False, False]
    is_present = verify_true_present(data_set)
    print(is_present)