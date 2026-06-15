def sort_list(data):
    data.sort()
    return data
if __name__ == '__main__':
    my_list = [5, 2, 8, 1, 9, 3]
    sorted_list = sort_list(my_list)
    print(sorted_list)