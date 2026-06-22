def check_all_strings(lst):
    return all(isinstance(item, str) for item in lst)

if __name__ == '__main__':
    sample_list = ['apple', 3.14, True, None]
    if not check_all_strings(sample_list):
        sample_list = [str(item) for item in sample_list]
    print(sample_list)