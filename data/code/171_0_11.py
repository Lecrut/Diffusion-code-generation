stores = [
    {"name": "Tech Hub", "description": "Electronics and gadgets"},
    {"name": "Bakery", "description": "Fresh bread and pastries"},
    {"name": "Pet Supplies", "description": "Dogs, cats, and birds"},
    {"name": "Bookstore", "description": "Novels, textbooks, and comics"}
]

filtered_stores = [store for store in stores if len(store["description"]) >= 10]

if __name__ == '__main__':
    print(filtered_stores)