def all_elements_match(lst):
    if not lst:
        return True
    first_element = lst[0]
    return all((element == first_element for element in lst))
if __name__ == '__main__':
    sample_values = [True, True, True, True]
    print(all_elements_match(sample_values))
    sample_values = [False, False, False, False]
    print(all_elements_match(sample_values))
    sample_values = [True, False, True, True]
    print(all_elements_match(sample_values))