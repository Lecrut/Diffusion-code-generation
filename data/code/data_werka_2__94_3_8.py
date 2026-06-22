def check_any_true(bool_list):
    status_map = {"has_true": any(bool_list)}
    return status_map["has_true"]

if __name__ == '__main__':
    sample_data = [False, False, True, False]
    output = check_any_true(sample_data)
    print(output)