def all_elements_match(lst):
    if not lst:
        return True
    first = lst[0]
    for item in lst[1:]:
        if item != first:
            return False
    return True

if __name__ == '__main__':
    sample_list = [True, True, True, True]
    print(all_elements_match(sample_list))