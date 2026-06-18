class ItemValidator:
    def validate(self, item):
        if not isinstance(item, dict) or 'name' not in item or 'price' not in item:
            raise ValueError("Item must be a dictionary with 'name' and 'price' keys.")
        if not isinstance(item['price'], (int, float)) or item['price'] <= 0:
            raise ValueError("Price must be a positive number.")
def create_item_list():
    items = [
        {'name': 'Laptop', 'price': 999.50},
        {'name': 'Mouse', 'price': 25.00},
        {'name': 'Keyboard', 'price': 75.0}
    ]
def main():
    validator = ItemValidator()
    validated_items = []
    for item in items:
        try:
            validator.validate(item)
            validated_items.append({'status': 'valid', **item})
        except ValueError as e:
            print(f"Validation failed for {item.get('name')}: {e}")
    return {'items_count': len(validated_items), 'data': validated_items}
if __name__ == '__main__':
    result = create_item_list()
    if isinstance(result, dict) and 'data' in result:
        print(f"Total valid items: {result['items_count']}")
        for item in result['data']:
            print(item)