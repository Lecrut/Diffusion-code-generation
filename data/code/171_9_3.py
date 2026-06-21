import csv

class Store:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def serialize_stores_to_csv(stores, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Name', 'Description'])
        for store in stores:
            writer.writerow([store.name, store.description])

if __name__ == '__main__':
    stores = [
        Store("Store A", "This is a \"great\" store with special characters like \n and \t."),
        Store("Store B", "Another store with a 'single quote'.")
    ]
    serialize_stores_to_csv(stores, 'output.csv')