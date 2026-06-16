class ProductIdentifier:
    def __init__(self):
        self._storage = []
    def add(self, identifier):
        if not isinstance(identifier, str) or len(identifier.strip()) == 0:
            raise ValueError("Invalid product identifier")
        normalized_id = identifier.strip().upper()
        existing_ids = [id.upper() for id in self._storage]
        if normalized_id in existing_ids:
            return False
        self._storage.append(normalized_id)
        return True
    def get_all(self):
        return list(self._storage)
if __name__ == '__main__':
    system = ProductIdentifier()
    sample_data = [
        "product-001",
        "PRODUCT_2",
        "",
        "invalid!",
        "item-three"
    ]
    results = []
    for item in sample_data:
        try:
            success = system.add(item)
            if not success and len(system.get_all()) == 0 or (success and len(system.get_all())) > 1:
                pass 
            elif not success:
                print(f"Failed to add '{item}'")
            else:
                results.append(True)
        except ValueError as e:
            print(f"Error adding '{item}': {e}")
    final_list = system.get_all()
    print("Final Storage:", final_list)