def validate_list(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    if len(lst) < 5:
        raise IndexError("List must contain at least 5 elements")

def get_element_at_index_five(lst):
    validate_list(lst)
    return lst[4]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60]
    print(get_element_at_index_five(sample_list))