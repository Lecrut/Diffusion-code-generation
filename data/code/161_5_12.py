def filter_items_by_status(items, status):
    if not isinstance(items, list) or not all(isinstance(item, str) for item in items):
        raise ValueError("Items must be a list of strings")
    if not isinstance(status, str):
        raise ValueError("Status must be a string")

    return (item for item in items if item == status)

if __name__ == '__main__':
    sample_items = ["active", "inactive", "pending", "active"]
    sample_status = "active"
    filtered_items = filter_items_by_status(sample_items, sample_status)
    print(list(filtered_items))