def get_first_element(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) == 0:
        raise ValueError("Input list must not be empty")
    return lst[0]

if __name__ == '__main__':
    sample_data = ["red", "green", "blue", "yellow"]
    first_item = get_first_element(sample_data)
    print(first_item)