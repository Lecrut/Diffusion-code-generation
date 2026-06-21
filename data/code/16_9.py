def get_first_element(lst):
    if not lst:
        return None
    return lst[0]

if __name__ == '__main__':
    print(get_first_element([1, 2, 3]))
    print(get_first_element([]))