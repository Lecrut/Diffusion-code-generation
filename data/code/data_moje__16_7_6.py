def get_leading_element(fixed_list):
    if not fixed_list:
        raise ValueError("List must not be empty")
    return fixed_list[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_leading_element(sample_list)
    print(result)