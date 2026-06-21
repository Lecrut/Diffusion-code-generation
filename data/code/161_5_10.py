STATUS_ACTIVE = "active"
ITEMS = [
    {"name": "item1", "status": STATUS_ACTIVE},
    {"name": "item2", "status": "inactive"},
    {"name": "item3", "status": STATUS_ACTIVE},
    {"name": "item4", "status": "pending"}
]

def filter_items_by_status(items, status):
    return (item for item in items if item["status"] == status)

if __name__ == '__main__':
    filtered_items = filter_items_by_status(ITEMS, STATUS_ACTIVE)
    print(list(filtered_items))