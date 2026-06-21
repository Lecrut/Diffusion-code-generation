def get_first_item(lst):
    if not lst:
        raise IndexError("Cannot get first item from an empty list")
    return lst[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_first_item(sample_list)
    print(result)