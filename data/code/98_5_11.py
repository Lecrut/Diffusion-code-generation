class SubscriptionManager:
    def __init__(self, items):
        self.items = items

    def classify_item(self, item):
        if item.get('status') == 'active':
            return 'Active'
        if item.get('type') == 'premium':
            return 'Premium'
        expiry = item.get('expiry_date')
        if expiry and expiry < '2023-01-01':
            return 'Expired'
        return 'Inactive'

    def process_all(self):
        results = []
        for item in self.items:
            classification = self.classify_item(item)
            new_item = dict(item)
            new_item['category'] = classification
            results.append(new_item)
        return results

if __name__ == '__main__':
    data = [
        {'id': 101, 'status': 'active', 'type': 'basic', 'expiry_date': '2025-01-01'},
        {'id': 102, 'status': 'inactive', 'type': 'premium', 'expiry_date': '2024-05-01'},
        {'id': 103, 'status': 'inactive', 'type': 'basic', 'expiry_date': '2022-12-31'},
        {'id': 104, 'status': 'inactive', 'type': 'basic', 'expiry_date': '2023-06-01'}
    ]
    manager = SubscriptionManager(data)
    output = manager.process_all()
    print(output)
    print(output[0]['category'])
    print(output[2]['category'])