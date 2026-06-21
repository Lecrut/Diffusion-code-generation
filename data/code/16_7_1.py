def get_first_element(items):
    return items[0] if items else None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    print(get_first_element(sample_list))