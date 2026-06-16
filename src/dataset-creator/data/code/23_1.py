class ProductIdentifier:
    def __init__(self):
        self.storage = []
    def add_product(self, product_id):
        if not isinstance(product_id, str) or len(product_id.strip()) == 0:
            raise ValueError("Product ID must be a non-empty string.")
        existing_ids = [p for p in self.storage]
        is_duplicate = any(p['id'] == product_id.strip() for p in existing_ids)
        if not is_duplicate:
            new_product = {'id': product_id.strip(), 'name': f"Product {len(self.storage) + 1}"}
            self.storage.append(new_product)
            return True, "Added successfully."
        return False, "Duplicate ID detected."
    def get_all_products(self):
        return [p['id'] for p in self.storage]
if __name__ == '__main__':
    system = ProductIdentifier()
    sample_ids = ["PROD-001", "", "  PROD-002  ", "invalid"]
    results = []
    for item in sample_ids:
        try:
            success, message = system.add_product(item)
            results.append(f"ID '{item}': {message}")
        except ValueError as e:
            results.append(f"Error processing ID '{item}': {e}")
    print("Final Product List:", system.get_all_products())