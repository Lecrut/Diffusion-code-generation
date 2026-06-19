def validate_list(lst):
    if not isinstance(lst, list):
        raise TypeError("Provided input is not a list.")
    if len(lst) == 0:
        raise ValueError("The list is empty.")

def get_first_element(lst):
    validate_list(lst)
    return lst[0]

if __name__ == '__main__':
    sample_list = [99, 198, 297]
    print(get_first_element(sample_list))