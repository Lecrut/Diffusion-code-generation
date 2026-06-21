class ItemManager:

    def __init__(self):
        self.items = {'apple': 100, 'banana': 150, 'cherry': 200}

    def get_item(self, key):
        return self.items.get(key)
if __name__ == '__main__':
    manager = ItemManager()
    print(f'Price of apple: {manager.get_item('apple')}')
    print(f'Price of banana: {manager.get_item('banana')}')
    print(f'Price of grape: {manager.get_item('grape')}')