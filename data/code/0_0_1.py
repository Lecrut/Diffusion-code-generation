def append_item(data: list, item):
    data.append(item)

if __name__ == '__main__':
    input_list = [1, 2, 3]
    new_item = 4
    append_item(input_list, new_item)
    output = input_list
    print(output)