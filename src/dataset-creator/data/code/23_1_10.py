class ProductIDManager:
    def __init__(self):
        self._storage = []
    def add_product(self, product_id: str) -> bool:
        if not isinstance(product_id, str) or len(product_id.strip()) == 0:
            return False
        cleaned_id = product_id.strip()
        for existing in self._storage:
            if existing['id'].lower() == cleaned_id.lower():
                return False
        new_entry = {
            'id': cleaned_id,
            'name': f"Product-{len(self._storage) + 1}",
            'status': 'active'
        }
        self._storage.append(new_entry)
        return True
    def get_product_by_id(self, product_id: str):
        for item in self._storage:
            if item['id'].lower() == product_id.lower():
                return item
        raise ValueError(f"Product ID '{product_id}' not found")
if __name__ == '__main__':
    manager = ProductIDManager()
    sample_ids = ["PROD-001", "prod-002", "invalid", "", "PROd-003"]
    for sid in sample_ids:
        result = manager.add_product(sid)
        print(f"Added '{sid}': {result}")
try:
    product = manager.get_product_by_id("PROD-001")
    if product:
        print(f"Fetched Product ID: {product['id']}, Name: {product['name']}")
except ValueError as e:
    print(e)