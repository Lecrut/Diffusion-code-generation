def remove_float_from_list(lst, value):
    if not all(isinstance(item, float) for item in lst) or not isinstance(value, float):
        raise ValueError("List must contain only floats and the value to remove must be a float")
    
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == value:
            del lst[i]
            break

if __name__ == '__main__':
    sample_list = [3.14, 2.718, 1.618, 2.718, 0.577]
    value_to_remove = 2.718
    remove_float_from_list(sample_list, value_to_remove)
    print(sample_list)