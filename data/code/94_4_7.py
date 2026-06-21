def check_existence(data_list):
    if not data_list:
        return False
    for flag in data_list:
        if flag:
            return True
    return False

if __name__ == '__main__':
    sample_data = [False, False, True, False]
    result = check_existence(sample_data)
    print(result)