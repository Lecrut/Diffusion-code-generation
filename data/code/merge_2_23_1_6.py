class ProductIdManager:
    def __init__(self):
        self._ids = set()
    def add_id(self, product_id):
        if not isinstance(product_id, str) or len(product_id.strip()) == 0:
            raise ValueError("Product ID must be a non-empty string.")
        cleaned_id = product_id.strip().upper()
        if self._ids.issubset(set(cleaned_id)):
            return False
        self._ids.add(cleaned_id)
        return True
    def get_ids(self):
        return list(self._ids)
if __name__ == '__main__':
    manager = ProductIdManager()
    sample_data = [
        "prod-123",
        "  PROD_456  ",
        "invalid",
        "",
        "PROD-789"
    ]
    results = []
    for item in sample_data:
        try:
            success = manager.add_id(item)
            if success and len(manager.get_ids()) > 0:
                results.append(f"Added: {manager._ids.pop()}")                                                                                                                                                                    
        except ValueError as e:
            results.append(f"Error adding '{item}': {e}")
    print("Validation Results:")
    for r in results:
        print(r)