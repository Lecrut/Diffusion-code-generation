def map_checklist_items(items: dict) -> dict:
    return {item: "Member" if item in ["apple", "banana", "cherry"] else "Non-Member" for item in items}

if __name__ == '__main__':
    sample_items = {"apple": True, "banana": False, "cherry": True, "date": False}
    print(map_checklist_items(sample_items))