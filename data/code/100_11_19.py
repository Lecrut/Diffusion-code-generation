def check_all_true(bool_list):
    return all(bool_list)

if __name__ == '__main__':
    sample_values = [True, True, True]
    print(check_all_true(sample_values))