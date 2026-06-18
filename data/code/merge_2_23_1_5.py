class ProductIdManager:
    def __init__(self):
        self.products = []
    def add_product(self, product_id: str) -> bool:
        if not isinstance(product_id, str) or len(product_id.strip()) == 0:
            return False
        cleaned_id = product_id.strip()
        for existing in self.products:
            if existing['id'] == cleaned_id:
                return False
        new_product = {
            'id': cleaned_id,
            'name': f"Product {len(self.products) + 1}",
            'created_at': None
        }
        self.products.append(new_product)
        print(f"Added product ID: {cleaned_id}")
        return True
    def get_all_products(self):
        for p in self.products:
            print(p['id'])
if __name__ == '__main__':
    manager = ProductIdManager()
    sample_ids = [
        "PROD-001",
        "",
        123,
        "   ",
        "PROD-999"
    ]
    for item in sample_ids:
        result = manager.add_product(item)
    print("\nAll Products:")
    manager.get_all_products()