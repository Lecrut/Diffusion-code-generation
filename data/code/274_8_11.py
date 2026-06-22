def print_items_until_condition(items, condition):
    index = 0
    while index < len(items) and not condition(items[index]):
        print(items[index])
        index += 1

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    condition = lambda x: x > 3
    print_items_until_condition(sample_list, condition)