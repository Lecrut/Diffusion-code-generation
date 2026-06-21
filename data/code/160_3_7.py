class ItemStore:
    def __init__(self, items):
        self.items = tuple(items)

    def search(self, query):
        return tuple(item for item in self.items if query.lower() in item.lower())

    def filter_by_length(self, length):
        return tuple(item for item in self.items if len(item) == length)

    def sort_alphabetically(self):
        return tuple(sorted(self.items))

if __name__ == '__main__':
    store = ItemStore(['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'])
    print("Search:", store.search('an'))
    print("Filter by Length 5:", store.filter_by_length(5))
    print("Sort Alphabetically:", store.sort_alphabetically())