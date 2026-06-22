def get_first_element(items):
    if not items:
        raise ValueError("List cannot be empty")
    return items[0]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    result = get_first_element(sample_data)
    print(result)