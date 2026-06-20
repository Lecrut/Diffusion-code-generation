class ItemProcessor:
    STATUS_ACTIVE = "Active"
    STATUS_PREMIUM = "Premium"
    STATUS_EXPIRED = "Expired"
    STATUS_INACTIVE = "Inactive"

    @staticmethod
    def process_item(item):
        if item.get('status') == 'active':
            return ItemProcessor.STATUS_ACTIVE
        elif item.get('type') == 'premium':
            return ItemProcessor.STATUS_PREMIUM
        elif item.get('expiry_date') and item.get('expiry_date') < '2023-01-01':
            return ItemProcessor.STATUS_EXPIRED
        else:
            return ItemProcessor.STATUS_INACTIVE

    @staticmethod
    def process_items(items):
        processed_list = []
        for item in items:
            result = {'id': item.get('id'), 'status': ItemProcessor.process_item(item)}
            processed_list.append(result)
        return processed_list

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Item A', 'status': 'active', 'type': 'standard', 'expiry_date': '2024-12-31'},
        {'id': 2, 'name': 'Item B', 'status': 'inactive', 'type': 'premium', 'expiry_date': '2022-12-31'}
    ]
    processed_data = ItemProcessor.process_items(sample_data)
    print(processed_data)