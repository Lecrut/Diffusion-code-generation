def has_true_element(bool_list):
    status_map = {True: "found", False: "not_found"}
    if not bool_list:
        return False
    result = any(bool_list)
    label = status_map.get(result, "unknown")
    return result

if __name__ == '__main__':
    sample_data = [False, False, False, True]
    output = has_true_element(sample_data)
    print(output)