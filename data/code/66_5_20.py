def is_sorted_ascending(lst):
    if not lst:
        return True
    previous_element = lst[0]
    for current_element in lst[1:]:
        if current_element < previous_element:
            return False
        previous_element = current_element
    return True
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(is_sorted_ascending(sample_list))