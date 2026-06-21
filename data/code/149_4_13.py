if __name__ == '__main__':
    input_list = [10, 20, 30, 40, 50]
    reversed_list = [input_list[i] for i in range(len(input_list)-1, -1, -1)]
    print(reversed_list)