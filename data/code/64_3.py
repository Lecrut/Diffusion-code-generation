if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 4, 5]
    target_value = 4
    last_index = my_list.index(target_value) if target_value in my_list else -1
    print(last_index)