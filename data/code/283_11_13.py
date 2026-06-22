def all_elements_are_strings(lst):
    return all(isinstance(x, str) for x in lst)

def convert_to_strings(lst):
    return [str(item) for item in lst]

def check_and_convert(data):
    if not all_elements_are_strings(data):
        data = convert_to_strings(data)
    return data

if __name__ == '__main__':
    sample_list = ['apple', 3.14, True, None]
    result = check_and_convert(sample_list)
    print(result)