stores = [
    {"name": "Bakery", "description": "A cozy bakery with delicious pastries."},
    {"name": "Tech Store", "description": "Selling latest electronics and gadgets."},
    {"name": "Toy Shop", "description": "Children's toys for all ages."},
    {"name": "Bookstore", "description": "Over 100,000 books to choose from."},
    {"name": "Hardware", "description": "Tools and equipment for do-it-yourself projects."}
]

def filter_stores_by_description_length(stores):
    return [store for store in stores if len(store["description"]) >= 10]

if __name__ == '__main__':
    filtered_stores = filter_stores_by_description_length(stores)
    for store in filtered_stores:
        print(f"Name: {store['name']}, Description: {store['description']}")