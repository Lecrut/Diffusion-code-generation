def print_list_items(data_list):
    index = 0
    while index < len(data_list):
        print(data_list[index])
        if data_list[index] == "hello":
            return
        index += 1

if __name__ == '__main__':
    sample_list = [1, "hello", 3.14, True]
    print_list_items(sample_list)