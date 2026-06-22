def validate_list(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) < 2:
        raise ValueError("List must contain at least two items")

def get_second_item(lst):
    validate_list(lst)
    return lst[1]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    second_item = get_second_item(sample_list)
    print(second_item)