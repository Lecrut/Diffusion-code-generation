def get_last_item(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    if len(lst) == 0:
        raise ValueError("List is empty.")
    return lst[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_item(sample_list)
    print(result)