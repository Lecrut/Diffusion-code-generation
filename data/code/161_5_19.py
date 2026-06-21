ITEMS = [
    "apple", "banana", "cherry", "date",
    "elderberry", "fig", "grape", "honeydew"
]

STATUS_ACTIVE = "active"

def filter_items_by_status(items, status):
    return (item for item in items if item.endswith(status))

if __name__ == '__main__':
    filtered_items = filter_items_by_status(ITEMS, STATUS_ACTIVE)
    print(list(filtered_items))