class ItemManager:

    def __init__(self):
        self.items = {'apple': 100, 'banana': 150, 'cherry': 200}

    def get_item(self, key):
        return self.items.get(key)
if __name__ == '__main__':
    manager = ItemManager()
    print(f'Value of apple: {manager.get_item('apple')}')
    print(f'Value of banana: {manager.get_item('banana')}')
    print(f'Value of grape: {manager.get_item('grape')}')