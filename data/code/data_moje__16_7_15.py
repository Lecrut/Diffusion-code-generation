def get_leading_element(fixed_list):
    if not fixed_list:
        return None
    return fixed_list[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result = get_leading_element(sample_list)
    print(result)