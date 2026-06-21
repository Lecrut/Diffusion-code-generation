def get_first_element(items):
    if not items:
        raise ValueError("List must be non-empty")
    return items[0]

if __name__ == '__main__':
    sample_data = [7, 8, 9]
    print(get_first_element(sample_data))