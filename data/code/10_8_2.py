def get_first_element(lst):
    result = lst[:1]
    print(result[0] if result else None)
    return result[0] if result else None

if __name__ == '__main__':
    mixed_list = [1, "hello", 3.14, True, None]
    get_first_element(mixed_list)