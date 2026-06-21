class ItemProcessor:
    def __init__(self, items):
        if not isinstance(items, list):
            raise ValueError("Items must be a list")
        self.items = list(items)

    def evaluate_status(self, item):
        if not isinstance(item, dict):
            raise ValueError("Each item must be a dictionary")
        
        status = None
        if item.get("is_active"):
            status = "Active"
        elif item.get("is_premium"):
            status = "Premium"
        elif item.get("is_expired"):
            status = "Expired"
        elif item.get("expiry_date"):
            try:
                from datetime import datetime
                expiry = datetime.strptime(item["expiry_date"], "%Y-%m-%d")
                if expiry < datetime.now():
                    status = "Expired"
                else:
                    status = "Valid"
            except (ValueError, TypeError):
                status = "Invalid Date"
        else:
            status = "Inactive"
        
        return status

    def process(self):
        results = []
        for item in self.items:
            status = self.evaluate_status(item)
            results.append({
                "id": item.get("id", "unknown"),
                "original_status": status
            })
        return results

if __name__ == '__main__':
    data = [
        {"id": 101, "is_active": True, "is_premium": False, "is_expired": False},
        {"id": 102, "is_active": False, "is_premium": True, "is_expired": False},
        {"id": 103, "is_active": False, "is_premium": False, "is_expired": True},
        {"id": 104, "is_active": False, "is_premium": False, "is_expired": False, "expiry_date": "2020-05-01"},
        {"id": 105, "is_active": False, "is_premium": False, "is_expired": False}
    ]
    processor = ItemProcessor(data)
    output = processor.process()
    print(output)