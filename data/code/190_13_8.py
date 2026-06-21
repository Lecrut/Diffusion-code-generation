def check_element_presence(target, data):
    return target in data

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    target_value = 30
    result = check_element_presence(target_value, sample_list)
    print(f"Does the list contain {target_value}? {result}")