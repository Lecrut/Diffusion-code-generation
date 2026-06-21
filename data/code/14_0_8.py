def get_third_element(lst):
    if len(lst) < 3:
        raise IndexError("List must have at least three items")
    return lst[2]

if __name__ == '__main__':
    result = get_third_element([1, 2, 3, 4, 5])
    print(result)