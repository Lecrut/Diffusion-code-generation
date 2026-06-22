def print_list_until_empty(data):
    while data:
        print(data.pop(0))

if __name__ == '__main__':
    sample_data = [1, "hello", 3.14, True]
    print_list_until_empty(sample_data)