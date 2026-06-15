def check_membership(main_list, target_item):
    return target_item in main_list
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    target = 30
    result = check_membership(sample_list, target)
    print(result)