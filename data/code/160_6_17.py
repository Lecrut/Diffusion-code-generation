ITEM_PRESENCE_MAP = {}

def add_item(item_name):
    ITEM_PRESENCE_MAP[item_name] = True

def remove_item(item_name):
    if item_name in ITEM_PRESENCE_MAP:
        del ITEM_PRESENCE_MAP[item_name]

def check_presence(item_name):
    return ITEM_PRESENCE_MAP.get(item_name, False)

if __name__ == '__main__':
    add_item('apple')
    add_item('banana')
    print(check_presence('apple'))
    print(check_presence('grape'))
    remove_item('apple')
    print(check_presence('apple'))