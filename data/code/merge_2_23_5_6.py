import sys
class ProductManager:
    def __init__(self):
        self.products = {}
    def add_product(self, title: str) -> bool:
        if not isinstance(title, str):
            raise TypeError("Product title must be a string.")
        stripped_title = title.strip()
        if len(stripped_title) == 0:
            return False
        self.products[stripped_title] = True
        return True
    def get_product(self, title: str) -> bool:
        cleaned_title = title.strip()
        return cleaned_title in self.products
def main():
    manager = ProductManager()
    sample_data = [
        "Laptop Pro 15",
        "",
        "   Wireless Mouse   ",
        None,
        "Mechanical Keyboard RGB"
    ]
    for item in sample_data:
        try:
            result = manager.add_product(item) if item is not None else False
            print(f"Processing '{item}' -> {'Added' if result else 'Skipped'}")
        except Exception as e:
            error_msg = f"Error occurred while processing input: {type(e).__name__}: {e}"
            print(error_msg)
    test_query_1 = "Laptop Pro 15"
    test_query_2 = "invalid product here"
    if manager.get_product(test_query_1):
        print(f"Found product in database.")
    else:
        print("Product not found in database.")
if __name__ == '__main__':
    main()