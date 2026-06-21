class ItemPresenceManager:
    def __init__(self):
        self.presence_dict = {}
    
    @staticmethod
    def add_item(item_name, presence_dict):
        presence_dict[item_name] = True
    
    @staticmethod
    def remove_item(item_name, presence_dict):
        if item_name in presence_dict:
            del presence_dict[item_name]
    
    @staticmethod
    def check_presence(item_name, presence_dict):
        return presence_dict.get(item_name, False)

if __name__ == '__main__':
    sample_items = ["apple", "banana", "cherry", "date"]
    presence_manager = ItemPresenceManager()
    for item in sample_items:
        if item:
            ItemPresenceManager.add_item(item, presence_manager.presence_dict)
    
    print(ItemPresenceManager.check_presence('apple', presence_manager.presence_dict))
    print(ItemPresenceManager.check_presence('grape', presence_manager.presence_dict))