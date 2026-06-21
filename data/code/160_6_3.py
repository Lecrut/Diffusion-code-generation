class ItemPresenceTracker:

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
    tracker = ItemPresenceTracker()
    tracker.add_item('apple')
    tracker.add_item('banana')
    print(tracker.check_presence('apple'))
    print(tracker.check_presence('grape'))
    tracker.remove_item('apple')
    print(tracker.check_presence('apple'))