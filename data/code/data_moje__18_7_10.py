def get_middle_item(lst):
    length = len(lst)
    index = length // 2
    return lst[index]

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    result = get_middle_item(data)
    print(result)