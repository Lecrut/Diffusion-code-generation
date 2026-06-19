class ListHandler:
    def __init__(self, lst):
        self.lst = lst
    
    def get_second_item(self):
        if len(self.lst) < 2:
            raise IndexError("List does not have a second item.")
        return self.lst[1]
    
    def has_second_item(self):
        return len(self.lst) >= 2

if __name__ == '__main__':
    sample_list = [8, 18, 28]
    handler = ListHandler(sample_list)
    if handler.has_second_item():
        print(handler.get_second_item())
    else:
        print("The list does not have a second item.")