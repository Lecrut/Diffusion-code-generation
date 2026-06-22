def are_all_strings(lst):
    return all(isinstance(item, str) for item in lst)

def convert_to_strings(lst):
    return [str(item) for item in lst]

def check_and_convert_list_elements(data):
    if not are_all_strings(data):
        data = convert_to_strings(data)
    return data

if __name__ == '__main__':
    sample_list = ['apple', 3.14, True, None]
    result = check_and_convert_list_elements(sample_list)
    print(result)