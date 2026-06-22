def get_leading_element(items):
    return items[0] if items else None

if __name__ == '__main__':
    sample_list = [42, 15, 99, 7]
    result = get_leading_element(sample_list)
    print(result)