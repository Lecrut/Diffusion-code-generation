def find_middle(lst):
    if not lst:
        return None
    length = len(lst)
    mid_index = length // 2
    if length % 2 == 1:
        return lst[mid_index]
    else:
        return lst[mid_index - 1], lst[mid_index]

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    even_list = [10, 20, 30, 40]

    odd_result = find_middle(odd_list)
    even_result = find_middle(even_list)

    print(odd_result)
    print(even_result)