class ListManager:
    def __init__(self, items):
        self.items = items

    def get_last_item(self):
        return self.items[-1]

    def display_list_and_last_item(self):
        print(f"List: {self.items}")
        last_item = self.get_last_item()
        print(f"Last item: {last_item}")

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    manager = ListManager(sample_list)
    manager.display_list_and_last_item()