def validate_item(item: dict) -> bool:
    required_keys = {'id', 'name'}
    return all(key in item for key in required_keys) and isinstance(item['id'], int)
class ItemListManager:
    def __init__(self):
        self.items = []
    def add_item(self, item_data: dict) -> bool:
        if not validate_item(item_data):
            return False
        new_id = max((i.get('id', 0) for i in self.items), default=0) + 1
        updated_item = {**item_data, 'id': new_id}
        self.items.append(updated_item)
        return True
    def get_items(self):
        return list(self.items)
if __name__ == '__main__':
    manager = ItemListManager()
    sample_data_1 = {'id': 0, 'name': 'Laptop'}
    sample_data_2 = {'id': -5, 'name': 'Mouse'}
    sample_data_3 = {'id': 10, 'name': 'Keyboard', 'extra_field': True}
    manager.add_item(sample_data_1)
    if not manager.add_item(sample_data_2):
        pass
    result = manager.add_item(sample_data_3)
    final_list = manager.get_items()