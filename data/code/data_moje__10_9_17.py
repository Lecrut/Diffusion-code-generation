def get_first_element(lst):
    if not lst:
        raise ValueError("List is empty")
    return lst[0]

if __name__ == '__main__':
    sample_list = [42, 'hello', 3.14, None]
    print(get_first_element(sample_list))