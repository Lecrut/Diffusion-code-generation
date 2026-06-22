def print_until_condition(items, condition):
    index = 0
    while index < len(items) and not condition(items[index]):
        print(items[index])
        index += 1

if __name__ == '__main__':
    items = ['apple', 'banana', 'cherry', 'date']
    condition = lambda item: item.startswith('c')
    print_until_condition(items, condition)