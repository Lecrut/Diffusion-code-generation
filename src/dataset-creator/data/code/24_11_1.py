import re
def validate_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None
class ItemListBuilder:
    def __init__(self):
        self.items = []
    def add_item(self, name: str, price: float, quantity: int, category: str, email: str) -> bool:
        if not isinstance(name, str) or len(name.strip()) == 0:
            return False
        try:
            price = float(price)
        except (ValueError, TypeError):
            return False
        if not isinstance(quantity, int) or quantity <= 0:
            return False
        categories = ['Electronics', 'Clothing', 'Food']
        if category not in categories:
            return False
        if not validate_email(email):
            return False
        item_data = {
            "name": name.strip(),
            "price": price,
            "quantity": quantity,
            "category": category,
            "email": email
        }
        self.items.append(item_data)
        return True
def main():
    builder = ItemListBuilder()
    sample_items = [
        ("Laptop", 999.50, 10, "Electronics", "user@example.com"),
        ("T-Shirt", 25.00, 50, "Clothing", "buyer@test.org"),
        (12345, -5.00, 5, "Food", "invalid-email"),
    ]
    results = []
    for item in sample_items:
        if len(item) != 5:
            continue
        is_valid = builder.add_item(*item)
        results.append({
            "input": item,
            "success": is_valid
        })
    final_list = {
        "total_count": len(builder.items),
        "valid_items": builder.items
    }
if __name__ == '__main__':
    pass