def get_first_element(items):
    if not items:
        raise ValueError("List is empty")
    return items[0]

if __name__ == '__main__':
    sample_data = [42, 100, 25, 7]
    print(get_first_element(sample_data))