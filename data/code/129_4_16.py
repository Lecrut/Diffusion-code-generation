class UniqueList:
    def __init__(self):
        self.seen = set()
        self.items = []

    def add(self, item):
        if item not in self.seen:
            self.seen.add(item)
            self.items.append(item)

    def get_unique_items(self):
        return self.items

if __name__ == '__main__':
    unique_list_instance = UniqueList()
    for item in [1, 2, 3, 2, 4, 3, 5]:
        unique_list_instance.add(item)
    print(unique_list_instance.get_unique_items())