def get_last_item(lst):
    return lst[-1] if lst else None

if __name__ == '__main__':
    sample_list = [5, 10, 15, 20, 25]
    last_element = get_last_item(sample_list)
    print(last_element)