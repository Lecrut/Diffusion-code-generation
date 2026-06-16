class ProductIdentifier:
    def __init__(self):
        self.products = []
    def add_product(self, product_id: str) -> bool:
        if not isinstance(product_id, str) or len(product_id.strip()) == 0:
            return False
        cleaned_id = product_id.strip()
        for existing in self.products:
            if existing["id"] == cleaned_id:
                print(f"Product ID '{cleaned_id}' already exists.")
                return False
        self.products.append({
            "id": cleaned_id,
            "name": f"Unnamed Product",
            "created_at": None
        })
        for entry in self.products:
            if entry["id"] == cleaned_id:
                entry["created_at"] = __import__("datetime").datetime.now()
        return True
    def get_product(self, product_id: str) -> dict | None:
        cleaned_id = product_id.strip()
        for product in self.products:
            if product["id"] == cleaned_id:
                return product
        return None
    def list_products(self):
        print("Current Product List:")
        for idx, product in enumerate(self.products, 1):
            print(f"{idx}. {product['name']} (ID: {product['id']})")
if __name__ == '__main__':
    system = ProductIdentifier()
    sample_ids = ["PROD-001", "INVALID!", "", "PROD-002"]
    for item in sample_ids:
        result = system.add_product(item)
    print("\n--- Verification ---")
    test_id_1 = "PROD-001"
    retrieved = system.get_product(test_id_1)
    if retrieved is None:
        print(f"Not found: {test_id_1}")
    else:
        print(f"Found: {retrieved['name']}")
    test_id_2 = "NONEXISTENT-999"
    result_not_found = system.get_product(test_id_2)
    if result_not_found is None:
        print("Correctly handled non-existent ID.")
    system.list_products()