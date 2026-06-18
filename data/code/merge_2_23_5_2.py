import sys
class ProductManager:
    def __init__(self):
        self.products = []
    def add_product(self, title):
        if not isinstance(title, str) or len(title.strip()) == 0:
            raise ValueError("Product title must be a non-empty string.")
        existing_titles = [p.title for p in self.products]
        if any(t.lower() == title.lower().strip() for t in existing_titles):
            raise DuplicateTitleError(f"Duplicate product found: '{title}'.")
        new_product = Product(title=title)
        self.products.append(new_product)
        return True
class DuplicateTitleError(Exception):
    pass
def main():
    manager = ProductManager()
    sample_data = [
        "Laptop Pro 15",
        "",
        None,
        "Wireless Mouse X200",
        "USB-C Hub Adapter",
        "Laptop Pro 15"
    ]
    for item in sample_data:
        try:
            if isinstance(item, str):
                result = manager.add_product(item)
                print(f"[OK] Added product.")
            else:
                raise TypeError("Invalid input type provided to add_product.")
        except ValueError as ve:
            print(f"[ERROR] {ve}")
        except DuplicateTitleError as de:
            print(f"[ERROR] {de}")
        except Exception as e:
            print(f"[CRITICAL] Unexpected error occurred: {e}", file=sys.stderr)
if __name__ == '__main__':
    main()