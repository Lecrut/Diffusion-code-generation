def check_existence(data_list):
    return bool(data_list) and any(data_list)

if __name__ == '__main__':
    sample_values = [False, False, True]
    print(check_existence(sample_values))