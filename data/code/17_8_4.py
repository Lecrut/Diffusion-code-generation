def get_last_element(lst):
    if not lst:
        raise ValueError("List must not be empty")
    return lst[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_last_element(sample_list))
    sample_list_empty = []
    try:
        get_last_element(sample_list_empty)
    except ValueError as e:
        print(e)