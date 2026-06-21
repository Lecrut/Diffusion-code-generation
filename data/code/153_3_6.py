def any_match(lst, target):
    return any(item == target for item in lst)

if __name__ == '__main__':
    sample_list = [3, 5, 8, 9]
    target_value = 8
    print(any_match(sample_list, target_value))