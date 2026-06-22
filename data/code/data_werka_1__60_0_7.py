def is_non_empty_list(data):
    return isinstance(data, list) and len(data) > 0

def find_last_element(data):
    if not is_non_empty_list(data):
        return None
    return data[-1]

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    last_element = find_last_element(sample_values)
    print(last_element)