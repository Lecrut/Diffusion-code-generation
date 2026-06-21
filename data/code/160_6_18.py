class ItemPresence:
    def __init__(self):
        self.presence_dict = {}
    
    def add_item(self, item_name):
        self.presence_dict[item_name] = True
    
    def remove_item(self, item_name):
        if item_name in self.presence_dict:
            del self.presence_dict[item_name]
    
    def check_presence(self, item_name):
        return self.presence_dict.get(item_name, False)

if __name__ == '__main__':
    item_tracker = ItemPresence()
    sample_items = ["strawberry", "raspberry", "blueberry", "grape"]
    for item in sample_items:
        if item:
            item_tracker.add_item(item)
    
    print(item_tracker.check_presence("strawberry"))
    print(item_tracker.check_presence("kiwi"))