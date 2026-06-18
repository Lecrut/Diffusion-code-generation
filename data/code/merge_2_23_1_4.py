class ProductIdentifier:
    def __init__(self):
        self.storage = []
    def add_product(self, product_id):
        if not isinstance(product_id, str) or len(product_id.strip()) == 0:
            raise ValueError("Product ID must be a non-empty string.")
        existing_ids = [p for p in self.storage]
        is_duplicate = any(p['id'] == product_id.strip() for p in existing_ids)
        if is_duplicate:
            return False
        new_product = {'id': product_id.strip(), 'name': f"Product {product_id}", 'status': 'active'}
        self.storage.append(new_product)
        print(f"Added Product ID: {product_id}")
        return True
    def get_products(self):
        return [p['id'] for p in self.storage]
if __name__ == '__main__':
    system = ProductIdentifier()
    sample_ids = ["PROD-001", "PROD-002", "", "invalid"]
    for item in sample_ids:
        try:
            result = system.add_product(item)
            if not result and len(system.get_products()) > 0:
                print(f"Duplicate or invalid entry skipped.")
        except ValueError as e:
            print(f"Validation Error: {e}")
    final_list = system.get_products()
    print("Final List:", final_list)