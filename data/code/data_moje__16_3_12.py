def get_first_item(lst):
    if not lst:
        raise IndexError("list index out of range")
    return lst[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_first_item(sample_list)
    print(result)