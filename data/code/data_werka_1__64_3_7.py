if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50, 40]
    target_value = 40
    last_index = max([i for i, x in enumerate(my_list) if x == target_value], default=-1)
    print(last_index)