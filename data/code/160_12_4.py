item_names = ('apple', 'banana', 'cherry')

def item_exists(name):
    return name in item_names
if __name__ == '__main__':
    print(item_exists('banana'))
    print(item_exists('orange'))