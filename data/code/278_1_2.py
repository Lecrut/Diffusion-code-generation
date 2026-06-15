def print_separately(iterable):
    for item in iterable:
        print(item)
if __name__ == '__main__':
    data1 = [1, 2, 3, 4]
    print_separately(data1)
    data2 = ('a', 'b', 'c')
    print_separately(data2)
    data3 = [10, 20.5, 300]
    print_separately(data3)