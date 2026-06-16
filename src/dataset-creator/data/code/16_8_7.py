def count_elements(lst):
    return len(lst)
if __name__ == '__main__':
    data = [1, "apple", 3.5, None, True]
    print(count_elements(data))
    empty_list = []
    print(count_elements(empty_list))