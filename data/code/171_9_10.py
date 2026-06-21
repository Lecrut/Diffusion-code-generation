import csv

class Store:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def serialize_stores(stores):
    with open('stores.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(['Name', 'Description'])
        for store in stores:
            writer.writerow([store.name, store.description])

if __name__ == '__main__':
    stores = [
        Store("Store A", "This is a \"sample\" description with special characters."),
        Store("Store B", "Another store with a newline.\nAnd another line.")
    ]
    serialize_stores(stores)