def print_items_separately(iterable):
    for item in iterable:
        print(item)
if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    print_items_separately(data1)
    data2 = ('a', 'b', 'c', 'd')
    print_items_separately(data2)
    data3 = [10.5, 20.1, 30.9]
    print_items_separately(data3)