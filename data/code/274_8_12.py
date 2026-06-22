MAX_ITERATIONS = 10

def print_list_items(data_list):
    index = 0
    while index < len(data_list) and index < MAX_ITERATIONS:
        print(data_list[index])
        index += 1

if __name__ == '__main__':
    sample_list = [1, "hello", 3.14, True, 5, 6, 7, 8, 9, 10, 11]
    print_list_items(sample_list)