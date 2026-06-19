class ListManager:
    def __init__(self, items):
        self.items = items

    def get_last_item(self):
        return self.items[-1]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    list_manager = ListManager(sample_list)
    
    print(f"List: {sample_list}")
    print(f"Last element via method call: {list_manager.get_last_item()}")