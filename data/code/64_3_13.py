if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target_value = 50
    last_index = next((i for i in range(len(my_list) - 1, -1, -1) if my_list[i] == target_value), -1)
    print(last_index)