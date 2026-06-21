class ItemFilter:
    STATUS_ACTIVE = "active"
    
    @staticmethod
    def filter_items(items, status):
        return (item for item in items if item.get("status") == status)

if __name__ == '__main__':
    sample_items = [
        {"name": "apple", "status": "active"},
        {"name": "banana", "status": "inactive"},
        {"name": "cherry", "status": "active"}
    ]
    filtered_items = ItemFilter.filter_items(sample_items, ItemFilter.STATUS_ACTIVE)
    print(list(filtered_items))