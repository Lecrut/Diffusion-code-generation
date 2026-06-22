def get_middle_item(lst):
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    result = get_middle_item(data)
    print(result)