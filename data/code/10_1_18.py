def get_first_element(lst):
    iterator = iter(lst)
    first = next(iterator)
    return first

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    result = get_first_element(sample_list)
    print(result)