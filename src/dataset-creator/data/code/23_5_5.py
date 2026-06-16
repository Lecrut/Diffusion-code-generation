import json
class ProductManager:
    def __init__(self):
        self.products = []
    def add_product(self, title):
        if not isinstance(title, str) or len(title.strip()) == 0:
            raise ValueError("Product title must be a non-empty string.")
        existing_titles = [p['title'].strip().lower() for p in self.products]
        new_title_lower = title.strip().lower()
        if any(existing_title == new_title_lower for existing_title in existing_titles):
            raise DuplicateTitleError(f"Product with title '{title}' already exists.")
        product_data = {
            "id": len(self.products) + 1,
            "title": title
        }
        self.products.append(product_data)
        return True
class DuplicateTitleError(Exception):
    pass
def main():
    manager = ProductManager()
    sample_titles = [
        "Laptop Pro X",
        "",
        None,
        12345,
        "Wireless Mouse Elite v2"
    ]
    for title in sample_titles:
        try:
            result = manager.add_product(title)
            print(f"[Success] Added product.") if result else print("[Error] Failed to add product.")
        except ValueError as ve:
            print(f"[Value Error] {ve}")
        except DuplicateTitleError as de:
            print(f"[Duplicate Title] {de}")
if __name__ == '__main__':
    main()