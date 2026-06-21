item_names = ('apple', 'banana', 'cherry')

def item_exists(item):
    return item in item_names
if __name__ == '__main__':
    print(item_exists('banana'))
    print(item_exists('orange'))