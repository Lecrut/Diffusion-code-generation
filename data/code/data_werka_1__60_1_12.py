def get_last_item(data):
    return data[-1] if data else None

class ListHandler:
    def __init__(self, items):
        self.items = items
    
    def get_last(self):
        return get_last_item(self.items)

if __name__ == '__main__':
    list_handler1 = ListHandler([10, 20, 30, 40])
    list_handler2 = ListHandler(['x', 'y', 'z'])
    list_handler3 = ListHandler([])
    
    print(list_handler1.get_last())
    print(list_handler2.get_last())
    print(list_handler3.get_last())