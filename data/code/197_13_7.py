checklist = {'apple', 'banana', 'cherry'}

def item_exists(item):
    return item in checklist
if __name__ == '__main__':
    print(item_exists('banana'))
    print(item_exists('grape'))