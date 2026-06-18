import re
class ProductIdentifier:
    def __init__(self, identifier):
        self.identifier = None
        if not isinstance(identifier, str) or len(identifier.strip()) == 0:
            raise ValueError("Invalid product identifier")
        cleaned_identifier = identifier.strip()
        if len(cleaned_identifier) < 3 or len(cleaned_identifier) > 50:
            raise ValueError(f"Product identifier must be between 3 and 50 characters long. Got {len(cleaned_identifier)}")
        pattern = r'^[A-Za-z][A-Za-z0-9_\-]{2,48}$'
        if not re.match(pattern, cleaned_identifier):
            raise ValueError("Product identifier must start with a letter and contain only alphanumeric characters, underscores, or hyphens.")
        self.identifier = cleaned_identifier
class ProductStorage:
    def __init__(self):
        self._products = {}
    def add(self, product_id: str) -> bool:
        if not isinstance(product_id, str):
            raise TypeError("Product ID must be a string")
        try:
            p = ProductIdentifier(product_id)
            if product_id in self._products:
                return False
            self._products[product_id] = {}
            return True
        except ValueError as e:
            print(f"Error adding {product_id}: {e}")
            return False
    def get(self, product_id: str) -> dict | None:
        if not isinstance(product_id, str):
            raise TypeError("Product ID must be a string")
        try:
            p = ProductIdentifier(product_id)
            if product_id in self._products:
                return self._products[product_id]
            else:
                print(f"Error getting {product_id}: Not found.")
                return None
        except ValueError as e:
            print(f"Error processing {product_id}: {e}")
    def list_all(self) -> dict[str, str]:
        result = {}
        for pid in self._products.keys():
            try:
                p = ProductIdentifier(pid)
                if isinstance(p.identifier, str):
                    result[pid] = f"ID: {p.identifier}"
            except ValueError as e:
                print(f"Error validating ID '{pid}': {e}")
        return result
if __name__ == '__main__':
    storage = ProductStorage()
    products = [
        "PRD-001",
        "ITEM_247",
        "INVALID!!ID",
        "ABC",
        "TOOL-X99"
    ]
    for pid in products:
        success = storage.add(pid)
        if not success and len(storage.list_all()) == 0:
            print(f"{pid} was rejected.")