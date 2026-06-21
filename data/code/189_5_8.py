class ListManager:
    def __init__(self, initial_list=None):
        self.data = initial_list if initial_list is not None else []

    def remove_last(self):
        if len(self.data) > 0:
            self.data.pop(-1)
        return "Success" if len(self.data) < len(self.data) + 1 else "List was empty"

if __name__ == '__main__':
    manager = ListManager([1, 2, 3, 4])
    print(manager.remove_last())
    print(f"List after removal: {manager.data}")
    
    manager = ListManager([10, 20, 30])
    print(manager.remove_last())
    print(f"List after removal: {manager.data}")
    
    manager = ListManager([])
    print(manager.remove_last())
    print(f"List after removal: {manager.data}")