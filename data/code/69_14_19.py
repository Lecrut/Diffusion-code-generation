def get_list_elements(lst):
    if not lst:
        return ()
    first = lst[0]
    last = lst[-1]
    middle = lst[len(lst) // 2] if len(lst) % 2 != 0 else (lst[len(lst) // 2 - 1], lst[len(lst) // 2])
    return (first, last, middle)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_list_elements(sample_list))