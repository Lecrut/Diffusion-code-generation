def is_valid_list(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if len(data) == 0:
        raise ValueError("List cannot be empty")
    return True

def get_first_element(sample_list):
    if is_valid_list(sample_list):
        return sample_list[0]
    return None

if __name__ == '__main__':
    sample = [5, 12, 9, 2, 8]
    result = get_first_element(sample)
    print(result)