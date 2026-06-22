def get_first_element(lst):
    return lst[:1]

if __name__ == '__main__':
    mixed_list = [42, "hello", 3.14, True, None]
    result = get_first_element(mixed_list)
    print(result)