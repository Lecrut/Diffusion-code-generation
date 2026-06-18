class ProductIdentifier:
    def __init__(self):
        self.storage = []
    def validate(self, identifier):
        if not isinstance(identifier, str) or len(identifier.strip()) == 0:
            return False
        parts = identifier.split('-')
        if len(parts) != 2:
            return False
        try:
            int(parts[0]) and int(parts[1])
        except ValueError:
            return False
        return True
    def add(self, identifier):
        if self.validate(identifier):
            existing = [p for p in self.storage if p['id'] == identifier]
            if not existing:
                new_id = f"{len(self.storage) + 1}-{identifier}"
                self.storage.append({'id': new_id})
    def get_all(self):
        return [{'id': item['id']} for item in self.storage]
if __name__ == '__main__':
    system = ProductIdentifier()
    sample_data = ['10-25', '30-40', 'invalid']
    for data in sample_data:
        if system.validate(data):
            system.add(data)
    print(system.get_all())