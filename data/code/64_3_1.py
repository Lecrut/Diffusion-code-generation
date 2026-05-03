if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 4, 5]
    target = 4
    result = my_list.index(target) if target in my_list else -1
    print(result)