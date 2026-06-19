def get_first_element(lst):
    return lst[0] if lst else None

if __name__ == '__main__':
    sample_list = [42, 3.14, 'hello']
    print(get_first_element(sample_list))