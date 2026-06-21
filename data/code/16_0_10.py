def get_first_element(items):
    if not items:
        raise ValueError("List must not be empty")
    return items[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    print(get_first_element(sample_list))