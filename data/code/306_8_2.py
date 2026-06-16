def print_iterable_with_separation(iterable):
    for item in iterable:
        print(item)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    tuple2 = ('a', 'b', 'c', 'd')
    list3 = [10.5, 20.1, 30.9]
    print("Printing list1:")
    print_iterable_with_separation(list1)
    print("-" * 10)
    print("Printing tuple2:")
    print_iterable_with_separation(tuple2)
    print("-" * 10)
    print("Printing list3:")
    print_iterable_with_separation(list3)