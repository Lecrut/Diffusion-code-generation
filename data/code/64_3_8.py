if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50, 40]
    target_value = 40
    last_index = my_list[::-1].index(target_value) if target_value in my_list else -1
    print(len(my_list) - last_index - 1)