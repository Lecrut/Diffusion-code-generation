from typing import Dict

def map_checklist_items(items: list) -> Dict[str, bool]:
    checklist = {
        "Item 1": False,
        "Item 2": True,
        "Item 3": False,
        "Item 4": True,
        "Item 5": False
    }
    return {item: checklist.get(item, False) for item in items}

if __name__ == '__main__':
    sample_items = ["Item 1", "Item 3", "Item 6"]
    print(map_checklist_items(sample_items))