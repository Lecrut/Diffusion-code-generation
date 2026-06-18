import sys
class ProductManager:
    def __init__(self):
        self.products = []
    def add_product(self, title: str) -> bool:
        if not isinstance(title, str):
            raise TypeError("Product title must be a string.")
        if len(title.strip()) == 0:
            raise ValueError("Product title cannot be empty after stripping whitespace.")
        existing_titles = [p.title for p in self.products]
        if any(t.lower() == title.lower().strip() for t in existing_titles):
            return False
        product_data = {
            "title": title.strip(),
            "id": len(self.products) + 1,
            "status": "active"
        }
        self.products.append(product_data)
        print(f"Product '{product_data['title']}' added successfully with ID: {product_data['id']}")
        return True
    def get_product_by_id(self, product_id: int) -> dict | None:
        if not isinstance(product_id, int):
            raise TypeError("Product ID must be an integer.")
        for idx, product in enumerate(self.products):
            if product["id"] == product_id:
                return {**product, "index": idx}
        return None
    def list_all_products(self) -> None:
        print("\n--- Current Product Collection ---")
        found_any = False
        for p in self.products:
            found_any = True
            print(f"ID: {p['id']}, Title: '{p['title']}' | Status: {p['status']}")
        if not found_any:
            print("No products registered.")
def main():
    manager = ProductManager()
    sample_titles = [
        "Wireless Bluetooth Headphones",
        "Ergonomic Office Chair",
        "",
        None,
        "   ",
        "Mechanical Keyboard RGB Backlit"
    ]
    try:
        for title in sample_titles:
            if isinstance(title, str):
                manager.add_product(title)
            else:
                print(f"Skipping invalid input type: {type(title).__name__}")
        retrieved = manager.get_product_by_id(1)
    except (TypeError, ValueError) as e:
        print(f"Error occurred during processing: {e}")
    if __name__ == '__main__':
        main()