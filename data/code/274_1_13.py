def print_items(collection):
    for element in collection:
        print(element)

if __name__ == '__main__':
    items = [10, "Python", 23.45, False]
    print_items(items)
    more_items = ('apple', 'banana', 'cherry')
    print_items(more_items)