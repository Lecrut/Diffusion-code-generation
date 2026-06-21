from collections import Counter

def validate_input(data_list):
    if not isinstance(data_list, list):
        raise ValueError("Input must be a list")
    return data_list

def count_elements(lst):
    lst = validate_input(lst)
    return dict(Counter(lst))

if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 3, 3]
    print(count_elements(sample_list))