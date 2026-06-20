def all_elements_equal(lst):
    if not lst:
        return True
    first = lst[0]
    return all((x == first for x in lst))
if __name__ == '__main__':
    print(all_elements_equal([True, True, True]))
    print(all_elements_equal([False, False, False]))
    print(all_elements_equal([True, False, True]))
    print(all_elements_equal([]))