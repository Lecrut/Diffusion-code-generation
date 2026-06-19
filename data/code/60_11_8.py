def get_last_element(lst):
    return lst[-1] if lst else None

if __name__ == '__main__':
    sample_list = [7, 17, 27, 37, 47]
    last_element = get_last_element(sample_list)
    print(last_element)