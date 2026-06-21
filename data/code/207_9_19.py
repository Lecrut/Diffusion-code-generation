from operator import attrgetter

class Item:
    def __init__(self, value):
        self.value = value

def find_max_by_attribute(items, attribute_name):
    if not items:
        raise ValueError("Input list cannot be empty")
    
    key_func = attrgetter(attribute_name)
    max_item = max(items, key=key_func)
    return max_item.value

if __name__ == '__main__':
    items = [Item(3), Item(1), Item(2)]
    max_value = find_max_by_attribute(items, 'value')
    print(max_value)