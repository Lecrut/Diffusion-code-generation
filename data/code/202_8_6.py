def find_max_mixed(lst):
    max_value = None
    for item in lst:
        if isinstance(item, (int, float)):
            if max_value is None or item > max_value:
                max_value = item
    return max_value

if __name__ == '__main__':
    sample_list = [3, 5.5, 'a', 2, 8]
    print(find_max_mixed(sample_list))