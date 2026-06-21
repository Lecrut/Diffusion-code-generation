class ListManager:
    def __init__(self, data_list):
        self.data_list = data_list

    def remove_last(self):
        if self.data_list:
            self.data_list.pop()
        else:
            print("List is empty")

if __name__ == '__main__':
    manager1 = ListManager([1, 2, 3, 4])
    manager1.remove_last()
    print(f"Updated list: {manager1.data_list}")
    
    manager2 = ListManager([])
    manager2.remove_last()
    print("No changes in empty list.")