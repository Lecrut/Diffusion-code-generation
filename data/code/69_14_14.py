FIRST = 0
LAST = -1

def get_elements(lst):
    length = len(lst)
    if not lst:
        return ()
    middle_index = (length - 1) // 2
    return (lst[FIRST], lst[LAST], lst[middle_index])
if __name__ == '__main__':
    sample_list = [5, 9, 3, 7, 1]
    print(get_elements(sample_list))